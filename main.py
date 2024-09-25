import actions
import time

def main():
    # Example action call

    ac = actions.Actions()
    # input("Press Enter to move the mouse to (100, 100) and click in 2 seconds")
    duration = int(input("Enter the duration of the move: "))


    start_time = time.time()
    ac.move(100, 100, duration)
    end_time = time.time()
    ac.click()
    
    elapsed_time = end_time - start_time
    print(f"Time taken for move: {elapsed_time} seconds")

if __name__ == "__main__":
    main()