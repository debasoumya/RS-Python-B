{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMw2pCqyNynSQO+ywVqn2wz",
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
        "<a href=\"https://colab.research.google.com/github/debasoumya/RS-Python-B/blob/main/Debasoumya%20/Qs_10.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EuBrPugAiQcX",
        "outputId": "05627352-96f6-4d83-9de5-1b2fb95fa69d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 4, 7]\n",
            "[2, 5, 8]\n",
            "[3, 6, 9]\n"
          ]
        }
      ],
      "source": [
        "a = [[1,2,3],[4,5,6],[7,8,9]]\n",
        "b=[[0,0,0],[0,0,0],[0,0,0]]\n",
        "for i in range(len(a)):\n",
        "\n",
        "   for j in range(len(a[0])):\n",
        "       b[j][i]=a[i][j]\n",
        "\n",
        "for r in b:\n",
        "   print(r)"
      ]
    }
  ]
}