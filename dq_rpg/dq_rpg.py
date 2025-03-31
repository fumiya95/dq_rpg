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
        elif choice == "5":  # クイックアタック
            if random.random() < 0.9:
                damage = max(0, player.attack - enemy.defense + random.randint(0, 3))
                print(f"{player.name}は『クイックアタック』を仕掛けた！")
            else:
                damage = 0
                print(f"{player.name}の『クイックアタック』は外れた！")