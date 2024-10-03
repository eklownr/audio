import argparse
import threading
import sounddevice as sd
import soundfile as sf


def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument(
    '-l', '--list-devices', action='store_true',
    help='show list of audio devices and exit')
args, remaining = parser.parse_known_args()
if args.list_devices:
    print(sd.query_devices())
    parser.exit(0)
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser])
#parser.add_argument(
#    'filename', metavar='FILENAME',
#    help='audio file to be played back')
parser.add_argument(
    '-d', '--device', type=int_or_str,
    help='output device (numeric ID or substring)')
args = parser.parse_args(remaining)


event = threading.Event()
current_frame = 0


def play_file(file):
    try:
        data, fs = sf.read(file)
    
        def callback(outdata, frames, time, status):
            global current_frame
            if status:
                print(status)
            chunksize = min(len(data) - current_frame, frames)
            outdata[:chunksize] = data[current_frame:current_frame + chunksize]
            if chunksize < frames:
                outdata[chunksize:] = 0
                raise sd.CallbackStop()
            current_frame += chunksize
    
        stream = sd.OutputStream(
            samplerate=fs, device=args.device, channels=data.shape[1],
            callback=callback, finished_callback=event.clear)#event.set
        with stream:
            event.wait(3)  # Wait until playback is finished
    except KeyboardInterrupt:
        parser.exit('\nInterrupted by user')
    except Exception as e:
        parser.exit(type(e).__name__ + ': ' + str(e))
    

print("Playing E oktav 2.   󰽰 󰝚 ")
play_file('../sounds/e2.mp3')
current_frame = 0

print("Playing A oktav 2.   󰽰 󰝚 ")
play_file('../sounds/a2.mp3')
current_frame = 0

print("Playing D oktav 3.   󰽰 󰝚 ")
play_file('../sounds/d3.mp3')
current_frame = 0

print("Playing G oktav 3.   󰽰 󰝚 ")
play_file('../sounds/g3.mp3')
current_frame = 0

print("Playing B oktav 3.   󰽰 󰝚 ")
play_file('../sounds/b3.mp3')
current_frame = 0

print("Playing E oktav 4.   󰽰 󰝚 ")
play_file('../sounds/e4.mp3')
current_frame = 0