from src.audio_generation import AudioGenerator


def main():

    generator = AudioGenerator(
        output_dir="Artifacts/audio_generation"
    )

    while True:

        text = input("\nEnter text (type 'exit' to quit): ")

        if text.lower() == "exit":
            break

        try:

            audio_path = generator.generate_audio(text)

            print("\nAudio generated successfully!")
            print(f"Saved at : {audio_path}")

        except Exception as e:

            print("\nError")
            print(e)

    return audio_path


if __name__ == "__main__":
    main()