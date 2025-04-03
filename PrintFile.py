def main():
  myFile = open("qbdata.txt", 'r')

  for line in myFile:
    info = line.split(",")
    td = info[12]
    name = info[0]
    rating = info[1]
    print(name, "had a ratin of", rating, "and threw", td, "touchdowns")
    print (line)

  myFile.close()


if __name__ == '__main__':
  main()
