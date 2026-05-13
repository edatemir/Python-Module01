# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_garden_data.py                                   :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: etemir <etemir@student.42istanbul.com.tr>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/05/03 14:12:57 by etemir             #+#    #+#             #
#   Updated: 2026/05/13 17:19:03 by etemir            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(
            f"{self.name}: "
            f"{self.height}cm, "
            f"{self.age} days old"
            )

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose:", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    rose.show()
    sunflower.show()
    cactus.show()
    