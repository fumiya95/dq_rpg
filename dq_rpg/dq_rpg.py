import random
import sys

# キャラクターの基本クラス
class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

# プレイヤークラス（勇者）
class Player(Character):
    def __init__(self, name):
        super().__init__(name, hp=100, attack=20, defense=10)
        self.exp = 0
        self.level = 1

    def gain_exp(self, amount):
        self.exp += amount
        print(f"{self.name}は{amount}の経験値を獲得！ (累計: {self.exp})")
        if self.exp >= self.level * 50:
            self.level += 1
            self.exp = 0
            self.max_hp += 20
            self.hp = self.max_hp
            self.attack += 5
            self.defense += 3
            print(f"{self.name}はレベルアップ！ 現在のレベル: {self.level}")

# 敵クラス
class Enemy(Character):
    pass

# 【ステップ11】 敵テンプレート（10種類）とランダム選択
enemy_templates = [
    {"name": "スライム",     "hp": 50,  "attack": 15, "defense": 5},
    {"name": "ゴブリン",     "hp": 60,  "attack": 18, "defense": 7},
    {"name": "オーク",       "hp": 80,  "attack": 20, "defense": 10},
    {"name": "バット",       "hp": 40,  "attack": 12, "defense": 4},
    {"name": "ウルフ",       "hp": 70,  "attack": 17, "defense": 8},
    {"name": "スケルトン",   "hp": 55,  "attack": 16, "defense": 6},
    {"name": "ゾンビ",       "hp": 65,  "attack": 14, "defense": 9},
    {"name": "ドラゴン",     "hp": 120, "attack": 25, "defense": 15},
    {"name": "ダークナイト", "hp": 90,  "attack": 22, "defense": 12},
    {"name": "魔法使い",     "hp": 45,  "attack": 30, "defense": 3}
]

def choose_enemy():
    template = random.choice(enemy_templates)
    return Enemy(template["name"], hp=template["hp"], attack=template["attack"], defense=template["defense"])

# 【ステップ18】 イントロストーリーの追加
def show_story():
    print("――――――――――――――――――――――――――――")
    print("昔々、遥かなる王国に一人の勇者がいた。")
    print("その勇者は、暗黒の勢力に立ち向かうため、")
    print("壮大な冒険の旅に出る決意を固めた。")
    print("――――――――――――――――――――――――――――\n")

# 【ステップ12～17】 バトルシステム（特殊技使用制限、攻撃命中率90％）
def battle(player, enemy):
    print("\n戦闘開始！")
    # 敵出現のナレーション【ステップ19】
    print(f"遠い森の奥から、恐るべき {enemy.name} が現れた！")
    
    # 技使用制限用辞書（技2～5は1戦中1回のみ）
    skill_usage = {"2": False, "3": False, "4": False, "5": False}

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

        let_hit = True
        if choice in ["1", "2", "3", "5"]:
            if random.random() >= 0.9:  # 90%命中、10%ミス
                let_hit = False

        if choice == "1":  # スラッシュ
            if let_hit:
                damage = max(0, player.attack - enemy.defense + random.randint(-2, 2))
                print(f"{player.name}は『スラッシュ』を使った！")
            else:
                damage = 0
                print(f"{player.name}の『スラッシュ』は外れた！")
        elif choice == "2":  # ファイアボール
            if let_hit:
                damage = max(0, int(player.attack * 1.5) - enemy.defense + random.randint(-2, 2))
                print(f"{player.name}は『ファイアボール』を放った！")
            else:
                damage = 0
                print(f"{player.name}の『ファイアボール』は外れた！")
        elif choice == "3":  # サンダーストーム
            if let_hit:
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
            if let_hit:
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

# 【ステップ20】 最終統合版
def main():
    show_story()  # イントロストーリー表示

    print("ドラゴンクエスト風RPGへようこそ！")
    name = input("あなたの勇者の名前を入力してください: ")
    player = Player(name)

    while True:
        enemy = choose_enemy()
        print(f"\n現れた敵は {enemy.name} です！")
        result = battle(player, enemy)
        if not player.is_alive():
            break
        choice = input("もう一度戦いますか？ (Y/N): ")
        if choice.lower() != "y":
            break
    print("ゲーム終了。ありがとうございました！")
    sys.exit()

if __name__ == "__main__":
    main()