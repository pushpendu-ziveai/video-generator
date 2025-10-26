#!/usr/bin/env python3.13
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
    
    output_name = input("Output filename (press Enter for 'my_video_script.txt'): ").strip()
    if not output_name:
        output_name = "my_video_script.txt"
    
    print(f"\n🎬 Generating video script: '{prompt}'")
    print("⏳ This may take 10-20 seconds...")
    
    # Generate the video script
    success = generator.generate_video(prompt, output_name)
    
    if success:
        print(f"\n🎉 Success! Your video script is ready: {output_name}")
        print("💡 This is a detailed storyboard that can be used to create an actual video!")
    else:
        print("\n😞 Video script generation failed. Check your AWS configuration.")

if __name__ == "__main__":
    main()