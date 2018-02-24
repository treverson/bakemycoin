# imported the requests library

import zipfile
import os 
import requests













#importating variables data
input_name = raw_input("Coin Name:\n pick up wesley\n") # User enters "orange"
globals()[input_name] = input_name
#maximum money
input_max = raw_input("Total money supply:")
globals()[input_max] = "1000000"
#EMISSION_SPEED_FACTOR
input_emission = raw_input("Emission curve:")
globals()[input_emission] = "1000000"
#Difficulty target
input_diff = raw_input("Difficulty target:")
globals()[input_diff] = "1000000"
#Block reward formula MISSION_SPEED_ in other file
input_block_reward = raw_input("Block reward formula:")
globals()[input_block_reward] = "1000000"
#P2P port
input_p2p = raw_input("P2P PORT:")
globals()[input_p2p] = "1000000"
#rpc port
input_rpc = raw_input("RPC PORT:")
globals()[input_rpc] = "1000000"
#Seed nodes
input_seed = raw_input("Seed Node:")
globals()[input_seed] = "1000000"
#Penalty free block size

#Address prefix
input_add_prefix = raw_input("Address Prefix:")
globals()[input_add_prefix] = "1000000"






#adding to code
with open("essential/tmp/CryptoNoteConfig.h", "r") as prev_file, open("essential/coins/cryptonote/src/CryptoNoteConfig.h", "w") as new_file:
    prev_contents = prev_file.readlines()
    #Now prev_contents is a list of strings and you may add the new line to this list at any position
    prev_contents.insert(76, '\n const char     CRYPTONOTE_NAME[]                             ="'+input_name+'"; \n ')
    prev_contents.insert(27, '\n const uint64_t MONEY_SUPPLY                                  = UINT64_C('+input_max+'); ')
    prev_contents.insert(29, '\n const unsigned EMISSION_SPEED_FACTOR                         = '+input_emission+';')
    prev_contents.insert(43, '\n const uint64_t DIFFICULTY_TARGET                             = '+input_diff+';')
    prev_contents.insert(90, '\n const int      P2P_DEFAULT_PORT                              = '+input_p2p+';')
    prev_contents.insert(90, '\n const int      RPC_DEFAULT_PORT                              = '+input_rpc+';')
    prev_contents.insert(110, '\n const std::initializer_list<const char*> SEED_NODES = {\n                         "'+input_seed+'",\n};\n')

    prev_contents.insert(17, '\n const uint64_t CRYPTONOTE_PUBLIC_ADDRESS_BASE58_PREFIX       = '+input_add_prefix+'; \n')



    new_file.write("".join(prev_contents))












#downloading neccary files if needed

print("Downloading files")
image_url = "https://github.com/cryptonotefoundation/cryptonote/archive/master.zip"
 
# URL of the image to be downloaded is defined as image_url
r = requests.get(image_url) # create HTTP response object

 
# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open("master.zip",'wb') as f:
 
    # Saving received content as a png file in
    # binary format
 
    # write the contents of the response (r.content)
    # to a new file in binary mode.
    f.write(r.content)


#unzip
print ("unziping")
dir_path = os.path.dirname(os.path.realpath(__file__))
zip_ref = zipfile.ZipFile( 'master.zip')
zip_ref.extractall(dir_path)
zip_ref.close()

#delete zip 
print ("cleaning")
os.remove("master.zip")

