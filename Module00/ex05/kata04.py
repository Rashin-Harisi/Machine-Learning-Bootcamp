#!/usr/bin/env python3

kata = (0, 4, 132.42222, 10000, 12345.67)

print(f"module_{kata[0]:2d}, "
      f"ex_{kata[1]:02d} : "
      f"{kata[2]:.2f}, "
      f"{kata[3]:.2e}, "
      f"{kata[4]:.2e}")