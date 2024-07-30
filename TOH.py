def tower_of_hanoi(n, source, auxiliary, target):
    """
    Solves the Tower of Hanoi problem.

    Parameters:
    n (int): Number of disks
    source (str): The source peg
    auxiliary (str): The auxiliary peg
    target (str): The target peg
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    
    # Move n-1 disks from source to auxiliary, so they are out of the way
    tower_of_hanoi(n - 1, source, target, auxiliary)
    
    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    
    # Move the n-1 disks from auxiliary to target
    tower_of_hanoi(n - 1, auxiliary, source, target)

# Example usage:
if __name__ == "__main__":
    n = 3  # Number of disks
    tower_of_hanoi(n, 'A', 'B', 'C')
