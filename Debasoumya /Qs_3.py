{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOLtIbsfsrZILygCTkzudlb",
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
        "<a href=\"https://colab.research.google.com/github/debasoumya/RS-Python-B/blob/main/Debasoumya%20/Qs_3.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "1Qp_4CvGSUIs"
      },
      "outputs": [],
      "source": [
        "l=[]\n",
        "a=int(input(\"enter no of element to be entered: \"))\n",
        "for i in range(0,a):\n",
        "    n=int(input(\"enter element of a list: \"))\n",
        "    l.append(n)\n",
        "print(l)\n",
        "l[-1]+=1\n",
        "print(l)"
      ]
    }
  ]
}