        if choice == "2":  # ファイアボール
            if random.random() < 0.75:  # 命中率75%
                damage = max(0, int(player.attack * 1.5) - enemy.defense + random.randint(-2, 2))
                print(f"{player.name}は『ファイアボール』を放った！")
            else:
                damage = 0
                print(f"{player.name}の『ファイアボール』は外れた！")
        elif choice == "3":  # サンダーストーム
            if random.random() < 0.5:  # 命中率50%
                damage = max(0, int(player.attack * 2) - enemy.defense + random.randint(-2, 2))
                print(f"{player.name}は『サンダーストーム』を発動した！")
            else:
                damage = 0
                print(f"{player.name}の『サンダーストーム』は失敗した！")
        elif choice == "4":  # ヒール
            heal = random.randint(15, 35)  # 回復量調整
            player.hp += heal
            if player.hp > player.max_hp:
                player.hp = player.max_hp
            print(f"{player.name}は『ヒール』で {heal} 回復した！")
            damage = 0
        # それ以外は同様