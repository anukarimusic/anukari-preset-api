import sys
from lib.anukari.proto import Model


def main():
  if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <input_file>")
    sys.exit(1)

  input_file = sys.argv[1]
  with open(input_file, "rb") as f:
    data = f.read()

  model = Model().parse(data)

  # This demo just prints the model in JSON format. If you want to use JSON
  # there is also a from_json() method. But note that the Model proto also
  # has its own API so you can manipulate it directly in Python, and this will
  # ensure that the data is always in a valid state.
  #
  # To get the binary output to write to a *.ank file, you can use bytes(model).
  # This example uses python-betterproto so be sure to check out their docs:
  # https://github.com/danielgtaylor/python-betterproto

  print(model.to_json(indent=2))


if __name__ == "__main__":
  main()
