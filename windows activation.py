import os

def kms_activation():
    # Display the link to the KMS Client Product Key page
    print("Please visit the following link to get your KMS Client Product Key:")
    print("https://learn.microsoft.com/en-us/windows-server/get-started/kms-client-activation-keys?tabs=server2022%2Cwindows10ltsc%2Cversion1803%2Cwindows81")
    print()  # Print a blank line for better readability

    # Ask the user to input the KMS Client Product Key
    kms_key = input("Please enter your KMS Client Product Key: ")

    # Integrate the key into the slmgr /ipk command
    command_1 = f"slmgr /ipk {kms_key}"

    # Execute the first command in CMD
    os.system(command_1)
    print("Product key installed successfully.")

    # Second command to set the KMS server
    command_2 = "slmgr /skms kms.digiboy.ir"

    # Execute the second command in CMD
    os.system(command_2)
    print("KMS server set to kms.digiboy.ir.")

    # Third command to activate Windows
    command_3 = "slmgr /ato"

    # Execute the third command in CMD
    os.system(command_3)
    print("Windows activated successfully.")

if __name__ == "__main__":
    kms_activation()
