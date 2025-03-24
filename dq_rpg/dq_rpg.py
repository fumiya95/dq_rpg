def battle(player, enemy):
    print("\n戦闘開始！")
    while player.is_alive() and enemy.is_alive():
        print(f"\n{player.name}のHP: {player.hp}/{player.max_hp}")
        print(f"{enemy.name}のHP: {enemy.hp}/{enemy.max_hp}")
        print("1: 攻撃する  2: 逃げる")
        choice = input("行動を選んでください: ")
        if choice == "1":
            damage = max(0, player.attack - enemy.defense + random.randint(-2, 2))
            enemy.take_damage(damage)
            print(f"{player.name}の攻撃！ {enemy.name}に {damage} のダメージ！")
        elif choice == "2":
            if random.random() < 0.5:
                print("逃げ切った！ バトル終了。")
                return False  # 逃走成功
            else:
                print("逃げられなかった！")
        else:
            print("無効な選択です。")
            continue

        if enemy.is_alive():
            damage = max(0, enemy.attack - player.defense + random.randint(-2, 2))
            player.take_damage(damage)
            print(f"{enemy.name}の攻撃！ {player.name}に {damage} のダメージ！")

    if player.is_alive():
        print(f"\n{player.name}の勝利！")
        return True
    else:
        print(f"\n{player.name}は倒れた...")
        return False

def main():
    print("ドラゴンクエスト風RPGへようこそ！")
    name = input("あなたの勇者の名前を入力してください: ")
    player = Player(name)

    while True:
        enemy = Enemy("スライム", hp=50, attack=15, defense=5)
        result = battle(player, enemy)
        if not player.is_alive():
            break

        choice = input("もう一度戦いますか？ (Y/N): ")
        if choice.lower() != "y":
            break
    print("ゲーム終了。ありがとうございました！")

if __name__ == "__main__":
    main()