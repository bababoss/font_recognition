from trdg.generators import (
    GeneratorFromDict,
    GeneratorFromRandom,
    GeneratorFromStrings,
    GeneratorFromWikipedia,
)

# The generators use the same arguments as the CLI, only as parameters
generator = GeneratorFromStrings(
    ["Hello, World!"],
#     blur=2,
#     random_blur=True
)
count=0
for img, lbl in generator:
    # Do something with the pillow images here.
    count+=1
    print(count)
    break
    