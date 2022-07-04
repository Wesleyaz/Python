from email.mime import base
import re

class ManipulatingFiles:
    def lookingExtensions():
        baseFilename = "file.txt"
        c_baseFilename = 'c_'+baseFilename
        cpp_baseFilename = 'cpp_'+baseFilename
        cs_baseFilename = 'cs_'+baseFilename
        hbaseFilename = open(baseFilename)
        hc_baseFilename = open(c_baseFilename, 'a+')
        hcpp_baseFilename = open(cpp_baseFilename, 'a+')
        hcs_baseFilename = open(cs_baseFilename, 'a+')

        for line in hbaseFilename:
            line = line.rsplit()[0]
            if line.endswith('.c'):
                hc_baseFilename.write(line+'\n')
            elif line.endswith('.cpp'):
                hcpp_baseFilename.write(line+'\n')
            elif line.endswith('.cs'):
                hcs_baseFilename.write(line+'\n')

        #hc_baseFilename.close()
        #hcpp_baseFilename.close()
        #hcs_baseFilename.close()

    def findingGif():
        baseFilename = "giffile.txt"
        gif_baseFilename = "gif_"+baseFilename
        hbaseFilename = open(baseFilename)
        hgif_baseFilename = open(gif_baseFilename, 'a')
        for line in hbaseFilename:
            line = line.rsplit()
            for word in line:
                gif = re.findall('\/([a-z0-9]+.GIF)', word)
                if gif:
                    hgif_baseFilename.write(gif[0]+'\n')

ManipulatingFiles.findingGif()