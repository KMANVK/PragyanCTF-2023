1. binwalk file pcap => nhận được các folder bên trong chứa hình ảnh chứa flag nhưng bị cắt ghép và đè pixel lên
2. Code dể lấy flag : 

        from PIL import Image

        import numpy as np
   
        import glob

        def merge_images(images):
   
            w, h = Image.open(images[0]).size
            instances = [Image.open(img).convert('RGB') for img in images]

            if w == 500:
               stack = np.vstack(instances)
            else:
               stack = np.hstack(instances)

            return Image.fromarray(stack)

         results = []
   
         for x in range(1, 11):
      
             images = sorted(
                    glob.glob(f'{x:0>2}/*')
             )
       
             results.append(merge_images(images))

         flag = Image.new('RGB', (500, 500))
         pix = flag.load()

         for res in results:
             for y in range(500):
                 for x in range(500):
                     if res.getpixel((x, y)) != (255, 0, 0):
                        pix[x, y] = res.getpixel((x, y))

         flag.save('flag.png')

#King pin p_ctf{TH3_D3V1L_0F_H3LL5_K1TCH3N_15_B4CK}
