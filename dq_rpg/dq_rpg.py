def battle(player, enemy):
    print("\n戦闘開始！")
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

        # プレイヤーの攻撃処理（技により効果が異なる）
        if choice == "1":  # スラッシュ
            # 通常攻撃
            damage = max(0, player.attack - enemy.defense + random.randint(-2, 2))
            print(f"{player.name}は『スラッシュ』を使った！")
        elif choice == "2":  # ファイアボール
            # 魔法攻撃（攻撃力1.5倍、命中率若干低め）
            if random.random() < 0.8:
                damage = max(0, int(player.attack * 1.5) - enemy.defense + random.randint(-2, 2))
                print(f"{player.name}は『ファイアボール』を放った！")
            else:
                damage = 0
                print(f"{player.name}の『ファイアボール』は外れた！")
        elif choice == "3":  # サンダーストーム
            # 強力攻撃（攻撃力2倍、命中率さらに低い）
            if random.random() < 0.6:
                damage = max(0, int(player.attack * 2) - enemy.defense + random.randint(-2, 2))
                print(f"{player.name}は『サンダーストーム』を発動した！")
            else:
                damage = 0
                print(f"{player.name}の『サンダーストーム』は失敗した！")
        elif choice == "4":  # ヒール
            # 自身を回復（攻撃ではなく回復効果）
            heal = random.randint(10, 30)
            player.hp += heal
            if player.hp > player.max_hp:
                player.hp = player.max_hp
            print(f"{player.name}は『ヒール』で {heal} 回復した！")
            damage = 0  # 敵にダメージは与えない
        elif choice == "5":  # クイックアタック
            # 早い攻撃（通常攻撃にわずかなボーナス）
            damage = max(0, player.attack - enemy.defense + random.randint(0, 3))
            print(f"{player.name}は『クイックアタック』を仕掛けた！")
        else:
            print("無効な選択です。")
            continue

        # 技が攻撃の場合、敵にダメージを与える
        if choice in ["1", "2", "3", "5"]:
            enemy.take_damage(damage)
            if damage > 0:
                print(f"{enemy.name}に {damage} のダメージ！")
            else:
                print("しかし、ダメージは与えられなかった。")

        # プレイヤーが回復した場合は敵へのダメージは無し
        # 敵がまだ生存していれば敵の攻撃
        if enemy.is_alive():
            enemy_damage = max(0, enemy.attack - player.defense + random.randint(-2, 2))
            player.take_damage(enemy_damage)
            print(f"{enemy.name}の攻撃！ {player.name}に {enemy_damage} のダメージ！")

    if player.is_alive():
        print(f"\n{player.name}の勝利！")
        # 勝利時に経験値加算（例：50exp）
        player.gain_exp(50)
        return True
    else:
        print(f"\n{player.name}は倒れた...")
        return False



# 既存のEnemyクラスはそのまま使うので、テンプレートを定義
enemy_templates = [
    {"name": "スライム",   "hp": 50,  "attack": 15, "defense": 5},
    {"name": "ゴブリン",   "hp": 60,  "attack": 18, "defense": 7},
    {"name": "オーク",     "hp": 80,  "attack": 20, "defense": 10},
    {"name": "バット",     "hp": 40,  "attack": 12, "defense": 4},
    {"name": "ウルフ",     "hp": 70,  "attack": 17, "defense": 8},
    {"name": "スケルトン", "hp": 55,  "attack": 16, "defense": 6},
    {"name": "ゾンビ",     "hp": 65,  "attack": 14, "defense": 9},
    {"name": "ドラゴン",   "hp": 120, "attack": 25, "defense": 15},
    {"name": "ダークナイト", "hp": 90, "attack": 22, "defense": 12},
    {"name": "魔法使い",   "hp": 45,  "attack": 30, "defense": 3}
]

def choose_enemy():
    # enemy_templates からランダムに1体選ぶ
    template = random.choice(enemy_templates)
    return Enemy(template["name"], hp=template["hp"], attack=template["attack"], defense=template["defense"])