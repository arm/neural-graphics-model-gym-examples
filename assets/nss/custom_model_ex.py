# SPDX-FileCopyrightText: <text>Copyright 2025 Arm Limited and/or
# its affiliates <open-source-office@arm.com></text>
# SPDX-License-Identifier: Apache-2.0


import torch
from ng_model_gym.core.model.base_ng_model import BaseNGModel
from ng_model_gym.core.model.layers.conv_block import ConvBlock
from ng_model_gym.core.model.model_registry import register_model
from ng_model_gym.core.utils.config_model import ConfigModel


class SimpleNN(torch.nn.Module):
    """Model backbone. 1x1 convolution."""

    def __init__(self, in_channels: int = 3):
        super().__init__()

        self.in_channels = in_channels

        self.conv = ConvBlock(
            in_channels=self.in_channels,
            out_channels=self.in_channels,
            kernel_size=1,
            padding=(0, 0),
            batch_norm=False,
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Forward pass"""
        return self.conv(x)


# Model must use the register_model decorator to be picked up
@register_model(name="custom_model", version="1")
class CustomModel(BaseNGModel):
    """Custom Model which inherits from BaseNGModel"""

    def __init__(self, params: ConfigModel):
        """Set up the model."""
        super().__init__()

        self.model_params = params
        self.neural_network = SimpleNN()

    def set_neural_network(self, neural_network: torch.nn.Module) -> None:
        """Set the model's neural network."""
        self.neural_network = neural_network

    def get_neural_network(self) -> torch.nn.Module:
        """Get the model's neural network."""
        return self.neural_network

    def preprocess(self, preprocess_input):
        """Preprocess the neural network inputs"""

        input_tensor = preprocess_input["colour_linear"].to(
            dtype=torch.float32, device=torch.device("cuda")
        )

        if input_tensor.max() > 1.0:
            input_tensor = input_tensor / 255.0

        return input_tensor

    def postprocess(self, inputs, model_output):
        """Postprocess the neural network outputs"""

        output = model_output

        output = torch.nn.functional.interpolate(
            output,
            size=inputs["motion"].shape[-2:],
            mode="bilinear",
            align_corners=False,
        )
        output = output[: inputs["motion"].shape[0]]

        return {"output": output, "out_filtered": output}

    def forward(self, inputs):
        """Forward pass"""

        input_tensor = self.preprocess(inputs)
        x = self.neural_network(input_tensor)
        outputs = self.postprocess(inputs, x)

        return outputs
