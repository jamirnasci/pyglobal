def read_fasta(file_path):
  sequence = ""
  header = ""

  try:
    with open(file_path, "r") as file:
      header = file.name
      for line in file:
        line = line.strip()
        if not line.startswith(">"):
          sequence += line

  except FileNotFoundError:
    print(f"Arquivo '{file_path}' não encontrado.")
    return None

  return header, sequence
