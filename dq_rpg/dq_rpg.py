def show_story():
    print("――――――――――――――――――――――――――――")
    print("昔々、遥かなる王国に一人の勇者がいた。")
    print("その勇者は、暗黒の勢力に立ち向かうため、")
    print("壮大な冒険の旅に出る決意を固めた。")
    print("――――――――――――――――――――――――――――\n")

def main():
    show_story()  # イントロストーリー表示

    print("ドラゴンクエスト風RPGへようこそ！")
    name = input("あなたの勇者の名前を入力してください: ")
    player = Player(name)

    while True:
        enemy = choose_enemy()  # ランダムに敵を選択
        print(f"\n現れた敵は {enemy.name} です！")
        result = battle(player, enemy)
        if not player.is_alive():
            break
        choice = input("もう一度戦いますか？ (Y/N): ")
        if choice.lower() != "y":
            break
    print("ゲーム終了。ありがとうございました！")
    sys.exit()


def battle(player, enemy):
    print("\n戦闘開始！")
    # スキル使用制限用辞書（技2～5は1回のみ使用可能）
    skill_usage = {"2": False, "3": False, "4": False, "5": False}
    
    print(f"遠い森の奥から、恐るべき {enemy.name} が現れた！")
    
    while player.is_alive() and enemy.is_alive():
        print(f"\n{player.name}のHP: {player.hp}/{player.max_hp}")
        print(f"{enemy.name}のHP: {enemy.hp}/{enemy.max_hp}")
        print("技を選択してください:")
        print("1: スラッシュ")
        print("2: ファイアボール")
        print("3: サンダーストーム")
        print("4: ヒール")
        print("5: クイックアタック")
        print("6: 逃げる")
        choice = input("行動を選んでください: ")
        
        if choice == "6":
            if random.random() < 0.5:
                print("逃げ切った！ バトル終了。")
                return False
            else:
                print("逃げられなかった！")
                continue
        
       
        if choice in ["2", "3", "4", "5"]:
            if skill_usage[choice]:
                print("その技は既に使用済みです。別の技を選んでください。")
                continue
            else:
                skill_usage[choice] = True

        # （以下、ステップ16で追加した命中率90%チェックと各技の処理を入れる）
        if choice == "1":  # スラッシュ
            if random.random() < 0.9:
                damage = max(0, player.attack - enemy.defense + random.randint(-2, 2))
                print(f"{player.name}は『スラッシュ』を使った！")
            else:
                damage = 0
                print(f"{player.name}の『スラッシュ』は外れた！")
        elif choice == "2":  # ファイアボール
            if random.random() < 0.9:
                damage = max(0, int(player.attack * 1.5) - enemy.defense + random.randint(-2, 2))
                print(f"{player.name}は『ファイアボール』を放った！")
            else:
                damage = 0
                print(f"{player.name}の『ファイアボール』は外れた！")
        elif choice == "3":  # サンダーストーム
            if random.random() < 0.9:
                damage = max(0, int(player.attack * 2) - enemy.defense + random.randint(-2, 2))
                print(f"{player.name}は『サンダーストーム』を発動した！")
            else:
                damage = 0
                print(f"{player.name}の『サンダーストーム』は失敗した！")
        elif choice == "4":  # ヒール
            heal = random.randint(15, 35)
            player.hp += heal
            if player.hp > player.max_hp:
                player.hp = player.max_hp
            print(f"{player.name}は『ヒール』で {heal} 回復した！")
            damage = 0
        elif choice == "5":  # クイックアタック
            if random.random() < 0.9:
                damage = max(0, player.attack - enemy.defense + random.randint(0, 3))
                print(f"{player.name}は『クイックアタック』を仕掛けた！")
            else:
                damage = 0
                print(f"{player.name}の『クイックアタック』は外れた！")
        else:
            print("無効な選択です。")
            continue

        if choice in ["1", "2", "3", "5"]:
            enemy.take_damage(damage)
            if damage > 0:
                print(f"{enemy.name}に {damage} のダメージ！")
            else:
                print("しかし、ダメージは与えられなかった。")

        if enemy.is_alive():
            enemy_damage = max(0, enemy.attack - player.defense + random.randint(-2, 2))
            player.take_damage(enemy_damage)
            print(f"{enemy.name}の攻撃！ {player.name}に {enemy_damage} のダメージ！")

    if player.is_alive():
        print(f"\n{player.name}の勝利！")
        player.gain_exp(50)
        return True
    else:
        print(f"\n{player.name}は倒れた...")
        return False