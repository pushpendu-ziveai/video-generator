#!/usr/bin/env python3
"""
Simple usage example for the AI Video Generator
"""

from video_generator import VideoGenerator

def main():
    """Quick demo of video generation capabilities."""
    print("🤖 AI Video Generator Demo")
    print("=" * 30)
    
    # Initialize the generator
    generator = VideoGenerator()
    
    # Get user input
    prompt = input("Enter your video description: ").strip()
    if not prompt:
        prompt = "A serene mountain lake at dawn"
        print(f"Using default prompt: {prompt}")
    
    output_name = input("Output filename (press Enter for 'my_video.mp4'): ").strip()
    if not output_name:
        output_name = "my_video.mp4"
    
    print(f"\n🎬 Generating video: '{prompt}'")
    print("⏳ This may take 30-60 seconds...")
    
    # Generate the video
    success = generator.generate_video(prompt, output_name)
    
    if success:
        print(f"\n🎉 Success! Your video is ready: {output_name}")
    else:
        print("\n😞 Video generation failed. Check your AWS configuration.")

if __name__ == "__main__":
    main()