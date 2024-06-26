import torchvision.models as models
import torch.nn as nn
        
class Classification(nn.Module):
    def __init__(self, num_classes=1):
        super(Classification, self).__init__()
        
        
        self.vgg = models.vgg19(pretrained=True)
        
        # Freeze convolutional layers
        for param in self.vgg.features.parameters():
            param.requires_grad = False
        
        # Replace fully connected layers
        self.vgg.classifier = nn.Sequential(
            nn.Linear(512 * 7 * 7, 4096),
            nn.ReLU(inplace=True),
            nn.Linear(4096, 4096),
            nn.ReLU(inplace=True),
            nn.Linear(4096, num_classes),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.vgg(x)
class Localization(nn.Module):
    def __init__(self, num_classes=4):
        super(Classification, self).__init__()
        
        
        self.vgg = models.vgg19(pretrained=True)
        
        # Freeze convolutional layers
        for param in self.vgg.features.parameters():
            param.requires_grad = False
        
        # Replace fully connected layers
        self.vgg.classifier = nn.Sequential(
            nn.Linear(512 * 7 * 7, 4096),
            nn.ReLU(inplace=True),
            nn.Linear(4096, 4096),
            nn.ReLU(inplace=True),
            nn.Linear(4096, num_classes),
        )

    def forward(self, x):
        return self.vgg(x)
    