
def main():
    # membuat
    li =[100,200,300,400,500]

    # menampilkan elemen di dalam list
    print(li[3])
    li.append(700)
    li.append(900)
    print("\nSetelah ditambah:")
    print(li)
    li.remove(100)
    print("\nSetelah dihapus:")
    print(li)
if __name__ =="__main__":
    main()

