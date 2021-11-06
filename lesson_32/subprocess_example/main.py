import subprocess

# capture output into variable
# output = subprocess.run(["ls", "-la"], capture_output=True, text=True)
# print(output.stdout)

#redirection output into the file
# with open("data.txt", "w") as file:
#     subprocess.run(["ls", "-la"], stdout=file, text=True)


# output = subprocess.run(["ls", "-la", "ddd"], stderr=subprocess.DEVNULL, text=True)
# print(output)

output = subprocess.Popen(["sleep", "5"])
print("FINISH")