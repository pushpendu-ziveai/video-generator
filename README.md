# AI Video Generator

A minimal Python agent that generates short videos using AWS Bedrock's Stable Video Diffusion model.

## Features

- 🎬 Generate videos from text prompts
- 🚀 Simple, clean Python 3.13 code
- ⚡ Minimal dependencies (only boto3)
- 🎯 Batch video generation support
- 📝 Easy to understand and modify

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure AWS credentials:**
   ```bash
   export AWS_ACCESS_KEY_ID="your_access_key"
   export AWS_SECRET_ACCESS_KEY="your_secret_key"
   export AWS_DEFAULT_REGION="us-east-1"
   ```

3. **Ensure Bedrock model access:**
   - Enable Stable Video Diffusion model in AWS Bedrock console
   - Verify you have proper IAM permissions

## Usage

### Generate Single Video
```python
from video_generator import VideoGenerator

generator = VideoGenerator()
generator.generate_video("A peaceful sunset over ocean waves", "my_video.mp4")
```

### Generate Multiple Videos
```python
prompts = [
    "A cat playing with a ball of yarn",
    "Rain drops falling on green leaves",
    "A bird flying through clouds"
]

generator.generate_multiple_videos(prompts, "output_videos/")
```

### Run Demo
```bash
python3 video_generator.py
```

## Code Structure

- `video_generator.py` - Main AI agent class and demo
- `requirements.txt` - Python dependencies  
- `.env.example` - AWS configuration template

## Configuration

The agent uses these default settings:
- Model: `stability.stable-video-diffusion-img2vid-v1:0`
- Region: `us-east-1`
- Steps: 25
- CFG Scale: 15

Modify the `VideoGenerator` class to customize these parameters.

## Notes

- Videos are typically 4 seconds long
- Output format: MP4
- Requires AWS Bedrock access with Stable Video Diffusion enabled
- Keep prompts descriptive but concise for best results