{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "' taş kağıt makas oyunu kuralları\\n\\n* kağıt taşı yener\\n* taş makası yener\\n* makas kağıdı yener '"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "''' taş kağıt makas oyunu kuralları\n",
    "\n",
    "* kağıt taşı yener\n",
    "* taş makası yener\n",
    "* makas kağıdı yener '''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Taş Kağıt Makas Oyununa Hoş geldiniz!\n",
      "-------------------------------------\n",
      "\n",
      "1 - Taş\n",
      "2 - Kağıt \n",
      "3 - Makas\n",
      "Oyundan çıkmak isterseniz bu değerler dışında bir değer giriniz\n",
      "Bilgisayarın Seçimi: 2\n",
      "\n",
      "Kazanan: Bilgisayar\n",
      "\n",
      "1 - Taş\n",
      "2 - Kağıt \n",
      "3 - Makas\n",
      "Oyundan çıkmak isterseniz bu değerler dışında bir değer giriniz\n",
      "\n",
      "\n",
      "Kullanıcı skoru 0 - Bilgisayarın skoru 100\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "player_score = computer_score = 0\n",
    "def print_result(comp_choice, winner):\n",
    "    print(f\"Bilgisayarın Seçimi: {comp_choice}\\n\\nKazanan: {winner}\")\n",
    "print(\"Taş Kağıt Makas Oyununa Hoş geldiniz!\\n\" + \"-\"*37)\n",
    "while True:\n",
    "    print(\"\\n1 - Taş\\n2 - Kağıt \\n3 - Makas\\nOyundan çıkmak isterseniz bu değerler dışında bir değer giriniz\")\n",
    "    player_choice = int(input(\"Seçiminizi yapınız\"))\n",
    "    computer_choice = random.choice([1, 2, 3])\n",
    "    if player_choice == computer_choice:\n",
    "        print(\"Beraber, yeniden oynayınız\")\n",
    "    elif player_choice == 1:\n",
    "        if computer_choice == 2:\n",
    "            print_result(computer_choice, \"Bilgisayar\")\n",
    "            computer_score += 100\n",
    "        elif computer_choice == 3:\n",
    "            print_result(computer_choice, \"Kullanıcı\")\n",
    "            player_score += 100\n",
    "    elif player_choice == 2:\n",
    "        if computer_choice == 1:\n",
    "            print_result(computer_choice, \"Kullanıcı\")\n",
    "            player_score += 100\n",
    "        elif computer_choice == 3:\n",
    "            print_result(computer_choice, \"Bilgisayar\")\n",
    "            computer_score += 100\n",
    "    elif player_choice == 3:\n",
    "        if computer_choice == 1:\n",
    "            print_result(computer_choice, \"Bilgisayar\")\n",
    "            computer_score += 100\n",
    "        elif computer_choice == 2:\n",
    "            print_result(computer_choice, \"Kullanıcı\")\n",
    "            player_score += 100\n",
    "    else:\n",
    "        break\n",
    "print(f\"\\n\\nKullanıcı skoru {player_score} - Bilgisayarın skoru {computer_score}\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.7 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.7"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "aee8b7b246df8f9039afb4144a1f6fd8d2ca17a180786b69acc140d282b71a49"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
