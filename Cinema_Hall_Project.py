{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "44d4309b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "------ WELCOME TO CINEMA ------\n",
      "\n",
      "Please enter your name: hgfh\n",
      "Please enter your age: 65\n",
      "Press 1 for Jawan\n",
      "Press 2 for Dunki\n",
      "Press 3 for Animal (A Rated)\n",
      "3\n",
      "---Animal---\n",
      "\n",
      "Press 1 for Recliner Seats @ 250\n",
      "Press 2 for Gold Seats @ 200\n",
      "Press 3 for Silver Seats @ 150\n",
      "3\n",
      "Please enter no of seats you want to book: 2\n",
      "2 Silver Seats Booked!\n",
      "-----Your total amount for seats is 300 -----\n",
      "Total Silver Seats left are 38\n",
      "\n",
      "Do you also want to add combo: (Yes/No) No\n",
      "Thank you!\n",
      "\n",
      "\n",
      "Do you want to book again: (Yes/No) Yes\n",
      "Press 1 for Recliner Seats @ 250\n",
      "Press 2 for Gold Seats @ 200\n",
      "Press 3 for Silver Seats @ 150\n",
      "2\n",
      "Please enter no of seats you want to book: 23\n",
      "23 Gold Seats Booked!\n",
      "-----Your total amount for seats is 4600 -----\n",
      "Total Gold Seats left are 17\n",
      "\n",
      "Do you also want to add combo: (Yes/No) Yes\n",
      "Please enter 1 for combo of Cold drink + Popcorn @ 200\n",
      "Please enter 2 for combo of Cold drink + Popcorn + French Fries @300\n",
      "2\n",
      "Please enter no of combos you want to add: 23\n",
      "23 Booked!\n",
      "-----Your total amount for 23 combo is 6900 -----\n",
      "\n",
      "Your total amount is 11500\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(\"------ WELCOME TO CINEMA ------\")\n",
    "print()\n",
    "name = input(\"Please enter your name: \")\n",
    "age = int(input(\"Please enter your age: \"))\n",
    "if age<18:\n",
    "    movie = int(input(\"\"\"Press 1 for Jawan\n",
    "Press 2 for Dunki\n",
    "\"\"\"))\n",
    "    if movie == 1:\n",
    "        print (\"---Jawan---\")\n",
    "    elif movie == 2:\n",
    "        print(\"---Dunki---\")\n",
    "    else:\n",
    "        print(\"Sorry! Incorrect input\")\n",
    "else:\n",
    "    movie = int(input(\"\"\"Press 1 for Jawan\n",
    "Press 2 for Dunki\n",
    "Press 3 for Animal (A Rated)\n",
    "\"\"\"))\n",
    "    if movie == 1:\n",
    "        print (\"---Jawan---\")\n",
    "    elif movie == 2:\n",
    "        print(\"---Dunki---\")\n",
    "    elif movie == 3:\n",
    "        print(\"---Animal---\")\n",
    "    else:\n",
    "        print(\"Sorry! Incorrect input\")\n",
    "        \n",
    "print()\n",
    "\n",
    "rec_seats = 20\n",
    "gold_seats = 40\n",
    "silver_seats = 40\n",
    "\n",
    "while True:\n",
    "\n",
    "    tos = int(input(\"\"\"Press 1 for Recliner Seats @ 250\n",
    "Press 2 for Gold Seats @ 200\n",
    "Press 3 for Silver Seats @ 150\n",
    "\"\"\"))\n",
    "    if tos == 1:\n",
    "    \n",
    "        nos = int(input(\"Please enter no of seats you want to book: \"))\n",
    "        if nos>rec_seats:\n",
    "            print(\"Sorry!\", nos, \"Seats are not available in Recliner\")\n",
    "            print (\"Total Recliner Seats left are\",rec_seats) \n",
    "        else:\n",
    "            print(nos, \"Recliner Seats Booked!\")\n",
    "            total1 = nos*250\n",
    "            print(\"-----Your total amount for seats is\",total1,\"-----\")\n",
    "            rec_seats = rec_seats - nos\n",
    "            print (\"Total Recliner Seats left are\",rec_seats) \n",
    "\n",
    "    if tos == 2:\n",
    "   \n",
    "        nos = int(input(\"Please enter no of seats you want to book: \"))\n",
    "        if nos>gold_seats:\n",
    "            print(\"Sorry!\", nos, \"Seats are not available in Gold\")\n",
    "            print (\"Total Gold Seats left are\",gold_seats)\n",
    "        else:\n",
    "            print(nos, \"Gold Seats Booked!\")\n",
    "            total1 = nos*200\n",
    "            print(\"-----Your total amount for seats is\",total1,\"-----\")\n",
    "            gold_seats = gold_seats - nos\n",
    "            print (\"Total Gold Seats left are\",gold_seats)\n",
    "\n",
    "    if tos == 3:\n",
    "    \n",
    "        nos = int(input(\"Please enter no of seats you want to book: \"))\n",
    "        if nos>silver_seats:\n",
    "            print(\"Sorry!\", nos, \"Seats are not available in Silver\")\n",
    "            print (\"Total Silver Seats left are\",silver_seats)\n",
    "        else:\n",
    "            print(nos, \"Silver Seats Booked!\")\n",
    "            total1 = nos*150\n",
    "            print(\"-----Your total amount for seats is\",total1,\"-----\")\n",
    "            silver_seats = silver_seats - nos\n",
    "            print (\"Total Silver Seats left are\",silver_seats)\n",
    "\n",
    "    print()\n",
    "\n",
    "    combo = str(input(\"Do you also want to add combo: (Yes/No) \"))\n",
    "    if combo == \"Yes\":\n",
    "        combo_type = int(input(\"\"\"Please enter 1 for combo of Cold drink + Popcorn @ 200\n",
    "Please enter 2 for combo of Cold drink + Popcorn + French Fries @300\n",
    "\"\"\"))\n",
    "        if combo_type == 1:\n",
    "            no_combo= int(input(\"Please enter no of combos you want to add: \"))\n",
    "            print (no_combo, \"Combo Booked!\")\n",
    "            total2 = no_combo*200\n",
    "            print (\"-----Your total amount for\",no_combo, \"combo is\", total2,\"-----\")\n",
    "            print()\n",
    "            print(\"Your total amount is\",total2+total1)\n",
    "            \n",
    "        elif combo_type == 2:\n",
    "            no_combo= int(input(\"Please enter no of combos you want to add: \"))\n",
    "            print (no_combo, \"Combo Booked!\")\n",
    "            total2 = no_combo*300\n",
    "            print (\"-----Your total amount for\",no_combo, \"combo is\", total2,\"-----\")\n",
    "            print()\n",
    "            print(\"Your total amount is\",total2+total1)\n",
    "        else:\n",
    "            print (\"Sorry! Invalid Input\")\n",
    "    elif combo == \"No\":\n",
    "        print (\"Thank you!\")\n",
    "    else:\n",
    "        print (\"Sorry Invalid Input\")\n",
    "    print()\n",
    "    \n",
    "    \n",
    "    \n",
    "    print()\n",
    "\n",
    "    \n",
    "    again = input(\"Do you want to book again: (Yes/No) \")\n",
    "    if again == \"No\":\n",
    "        print(\"Your total amount is\",total1)\n",
    "        print(\"Have a great day!\")\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8763f988",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c7e83365",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dd853fe7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8e6eeb23",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e2ef9617",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "39a72b7a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9fe1ece7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "204a5078",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7a05db95",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b930d367",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b3d804ca",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e9031d89",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e8bc4063",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d82cb9ba",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bd271dfb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "61f3fb64",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7b43caa5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "17e50e98",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a2b95aaa",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96ac09e1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "15b27e6b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "15e5a7b1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f6db1cc",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "330a1b1d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7a838680",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b383a765",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4f11c6a2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1e8199e5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8701767b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "45187c30",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a0399fff",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "93b8cc84",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fa6b3b29",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8642599f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "28a5b779",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8cc9ae30",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aeb6f0b4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "02b7c8e7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "45fc7cca",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b49a7a48",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c16cc82a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5b317b4c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1ab425aa",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bc583a3a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "55edaeb7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ea2c5cae",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3c3d24ba",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4d12fb9e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "44ca6bc5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5f80f0de",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b0ecbf9d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b5729ab",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a98295d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3de5c6d2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b79877ad",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f15e0f8e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "88aca12d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "94be3a45",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "78b43607",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "352acf6f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5eed4eaa",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
