{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPYaweL7MwQNnvfsphND6/w",
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
        "<a href=\"https://colab.research.google.com/github/debasoumya/RS-Python-B/blob/main/Debasoumya%20/Qs_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "s=input(\"enter a string: \")\n",
        "s=s.replace(\" \",\"\")\n",
        "n=\"\"\n",
        "for i in s:\n",
        "    if i not in n:\n",
        "        n=n+i\n",
        "a=sorted(n)\n",
        "for i in a:\n",
        "    print(i,\"->\",s.count(i))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-ENEMzgMMZbP",
        "outputId": "4432ce6f-0d42-4c44-c01e-b529536c132c"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter a string: debasoumya\n",
            "a -> 2\n",
            "b -> 1\n",
            "d -> 1\n",
            "e -> 1\n",
            "m -> 1\n",
            "o -> 1\n",
            "s -> 1\n",
            "u -> 1\n",
            "y -> 1\n"
          ]
        }
      ]
    }
  ]
}