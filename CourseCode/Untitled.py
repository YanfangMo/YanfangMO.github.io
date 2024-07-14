{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3086acf3-3e9a-4b4f-a2db-c34ee9aa3375",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hellodd World!\n",
      "11\n",
      "The running time of sum1 is 0.00017690658569335938.\n",
      " 10% "
     ]
    }
   ],
   "source": [
    "def hello() :\n",
    "    print(\"Hellodd World!\")\n",
    "\n",
    "def sum_1(a,b,c):\n",
    "    return a + b + c\n",
    "\n",
    "import time\n",
    "\n",
    "hello()\n",
    "\n",
    "start = time.time()\n",
    "x = sum_1(2,5,4)\n",
    "print(x)\n",
    "end = time.time()\n",
    "print('The running time of sum1 is {}.'.format(end-start))\n",
    "\n",
    "\n",
    "for i in range(11):\n",
    "    print(\"\\r{:3}%\".format(i),end=' ')\n",
    "    time.sleep(0.1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b11192f4-f459-4806-b4c9-eeeb82034bfa",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
