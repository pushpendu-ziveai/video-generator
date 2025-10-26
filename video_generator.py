#!/usr/bin/env python3
"""
AI Video Generator using AWS Bedrock
Minimal implementation for generating short videos from text prompts.
"""

import boto3
import json
import base64
import os
from typing import Optional


class VideoGenerator:
    """Simple AI agent for video generation using AWS Bedrock."""
    
    def __init__(self, region: str = 'us-east-1'):
        """Initialize the video generator with AWS Bedrock client."""
        self.bedrock = boto3.client('bedrock-runtime', region_name=region)
        self.model_id = 'stability.stable-video-diffusion-img2vid-v1:0'
    
    def generate_video(self, prompt: str, output_path: str = 'generated_video.mp4') -> bool:
        """
        Generate a short video from text prompt.
        
        Args:
            prompt: Text description of the video to generate
            output_path: Path to save the generated video
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Prepare the request payload
            body = {
                "text_prompts": [{"text": prompt}],
                "cfg_scale": 15,
                "motion_bucket_id": 127,
                "seed": 0,
                "steps": 25
            }
            
            # Call Bedrock API
            response = self.bedrock.invoke_model(
                body=json.dumps(body),
                modelId=self.model_id,
                accept='application/json',
                contentType='application/json'
            )
            
            # Parse response
            response_body = json.loads(response.get('body').read())
            
            if 'artifacts' in response_body and response_body['artifacts']:
                # Decode and save video
                video_data = base64.b64decode(response_body['artifacts'][0]['base64'])
                
                # Ensure output directory exists
                os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
                
                with open(output_path, 'wb') as f:
                    f.write(video_data)
                
                print(f"✅ Video generated successfully: {output_path}")
                return True
            else:
                print("❌ No video generated in response")
                return False
                
        except Exception as e:
            print(f"❌ Error generating video: {str(e)}")
            return False
    
    def generate_multiple_videos(self, prompts: list, output_dir: str = 'videos'):
        """Generate multiple videos from a list of prompts."""
        os.makedirs(output_dir, exist_ok=True)
        
        for i, prompt in enumerate(prompts):
            output_path = os.path.join(output_dir, f'video_{i+1}.mp4')
            print(f"🎬 Generating video {i+1}/{len(prompts)}: {prompt[:50]}...")
            self.generate_video(prompt, output_path)


def main():
    """Main function to demonstrate video generation."""
    # Initialize generator
    generator = VideoGenerator()
    
    # Example prompts for short videos
    prompts = [
        "A peaceful sunset over ocean waves",
        "A cat playing with a ball of yarn",
        "Rain drops falling on green leaves"
    ]
    
    # Generate single video
    print("🚀 Starting AI Video Generation...")
    generator.generate_video(prompts[0], "sunset_video.mp4")
    
    # Generate multiple videos
    print("\n🎯 Generating multiple videos...")
    generator.generate_multiple_videos(prompts)


if __name__ == "__main__":
    main()