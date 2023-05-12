from sys import exit

def magic_room():
    print("恭喜开启魔法门！希望祝多少岁生日快乐呢？")

    choice = input(">")

    if "18" in choice:
        how_much = int(choice)
        print("恭喜开启进阶版剧情~ 送上生日蛋糕！收下诚挚祝福。"
              "Happy Birthday! Happy Everyday!")
        exit(0)
    else:
        print("再猜一次吧~")
        magic_room()

def left_room():
    print("今天是开心的一天")
    print("希望每天都能这么开心")
    print("祝看到祝福的你也会这样开心")
    print("希望怎么送上祝福吗？")
    print("除草/兜风/生日快乐/.../棒棒")
    door_moved = False

    while True:
        choice = input(">")

        if choice == "除草":
            end("草丛很清新还长满了小花。先出去遛弯了。再试一次吧")
        if choice == "兜风":
            end("阳光满满的一天。先下车了。再试一次吧")
        elif choice == "生日快乐" and not door_moved:
            print("很开心地打开门")
            print("再来一句魔法祝福吧~")
            door_moved = True
        elif choice == "棒棒" and door_moved:
            end("送出666游轮。还没吃到蛋糕，再试一次吧。")
        elif choice == "要一直开心下去哦" and door_moved:
            magic_room()
        else:
            print("打了一个魔法响指，来再试一下")

def right_room():
    print("我在包饺子。")
    print("希望刷火箭还是送祝福呢？")

    choice = input(">")

    if "刷火箭" in choice:
        start()
    elif "送祝福" in choice:
        end("谢谢！收下诚挚祝福。Happy Birthday!还有其他支线剧情，再试一次吧")
    else:
        right_room()

def end(why):
    print(why, "(#^.^#)")
    exit(0)

def start():
    print("欢迎看到这里:) 今天是我的生日。")
    print("这里有一扇左边门和右边门。")
    print("希望推开那一扇门去庆祝？")

    choice = input(">")

    if choice == '左':
        left_room()
    elif choice == '右':
        right_room()
    else:
        end("Best is yet to come! Begin Again!")

start()
