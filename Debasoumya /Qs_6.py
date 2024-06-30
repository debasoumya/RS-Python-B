{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP+TZySQ2y+HIneFnWfae3b",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/debasoumya/RS-Python-B/blob/main/Debasoumya%20/Qs_6.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "e7rIRJOmVIzK"
      },
      "outputs": [],
      "source": [
        "N=int(input(\"Enter the number of elements : \"))\n",
        "A=[]\n",
        "min=0\n",
        "max=0\n",
        "for i in range(N):\n",
        "  b=int(input(\"Enter the element : \"))\n",
        "  A.append(b)\n",
        "\n",
        "x=sorted(A)\n",
        "for i in range(N):\n",
        "  if isPrime(x[i]):\n",
        "   min=x[i]\n",
        "   break\n",
        "for i in range(N-1,0,-1):\n",
        "\n",
        "  if isPrime(x[i]):\n",
        "    max=x[i]\n",
        "if max==min and max!=0 and min!=0:\n",
        "  print(\"Difference = \",(max-min))\n",
        "else:\n",
        "  print(\"Difference = \",min)\n",
        "if max==min and max==0:\n",
        "  print(1)"
      ]
    }
  ]
}