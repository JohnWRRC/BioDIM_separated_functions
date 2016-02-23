import grass.script as grass
import os

def export_raster_from_grass(landscape_grassname_habmat, landscape_grassname_hqmqlq, landscape_grassname_habdist, landscape_grassname_habmat_pid, landscape_grassname_habmat_areapix, landscape_grassname_hqmqlq_quality, landscape_grassname_hqmqlq_AREAqual, landscape_grassname_frag_pid, landscape_grassname_frag_AREApix,landscape_grassname_frag_AREAqual, landscape_grassname_dila01clean_pid, landscape_grassname_dila01clean_AREApix,landscape_grassname_dila01clean_AREAqual, landscape_grassname_dila02clean_pid, landscape_grassname_dila02clean_AREApix,landscape_grassname_dila02clean_AREAqual,defaultDir,inputDir,tempDir):
    '''This function read a set of filenames and export it from grass Mapsets 
    For this simulations, filename will be a list of _habmat, 
    _dist, _funcArea (several), _effectiveFuncArea
    '''

    ''' 
    An update was done in jan 2014 to fit with the new versions of GRASS 6.4.3
    
    '''
    
    #mycommands=[]
    
    os.chdir(defaultDir)
    os.chdir(inputDir)    
    grass.run_command("r.colors", map=landscape_grassname_habmat+'@MS_HABMAT', rules='_habmat_color.txt')
    
    os.chdir(defaultDir)
    os.chdir(tempDir)    
    grass.run_command('r.out.ascii', input=landscape_grassname_habmat+'@MS_HABMAT', output='random_landscape_habmat.asc')
    grass.run_command('r.out.png', input=landscape_grassname_habmat+'@MS_HABMAT', output='random_landscape_habmat.png')
    
    grass.run_command('r.colors.stddev', input=landscape_grassname_habdist+'@MS_HABMAT_DIST')
    grass.run_command('r.out.ascii', input=landscape_grassname_habdist+'@MS_HABMAT_DIST', output='random_landscape_habdist.asc')
    grass.run_command('r.out.png', input=landscape_grassname_habdist+'@MS_HABMAT_DIST', output='random_landscape_habdist.png')
    
    grass.run_command('r.out.ascii',input=landscape_grassname_hqmqlq+'@MS_HQMQLQ', output='random_landscape_hqmqlq.asc')
    grass.run_command('r.out.png', input=landscape_grassname_hqmqlq+'@MS_HQMQLQ', output='random_landscape_hqmqlq.png')
    
    ##---------------------------------
    grass.run_command('r.out.ascii', input=landscape_grassname_habmat_pid+'@MS_HABMAT_PID',  output='random_landscape_habmat_pid.asc', null=0)
    grass.run_command('r.out.png', input=landscape_grassname_habmat_pid+'@MS_HABMAT_PID', output='random_landscape_habmat_pid.png')

    grass.run_command('r.out.ascii', input=landscape_grassname_habmat_areapix+'@MS_HABMAT_AREA', output='random_landscape_habmat_areapix.asc', null=0)
    grass.run_command('r.out.png', input=landscape_grassname_habmat_areapix+'@MS_HABMAT_AREA', output='random_landscape_habmat_areapix.png')

    grass.run_command('r.out.ascii', input=landscape_grassname_hqmqlq_quality+'@MS_HQMQLQ_AREAqual', output='random_landscape_hqmqlq_quality.asc', null=0)
    grass.run_command('r.out.png', input=landscape_grassname_hqmqlq_quality+'@MS_HQMQLQ_AREAqual', output='random_landscape_hqmqlq_quality.png')
    
    grass.run_command('r.out.ascii', input=landscape_grassname_hqmqlq_AREAqual+'@MS_HQMQLQ_AREAqual', output='random_landscape_hqmqlq_AREAqual.asc', null=0)
    grass.run_command('r.out.png', input=landscape_grassname_hqmqlq_AREAqual+'@MS_HQMQLQ_AREAqual', output='random_landscape_hqmqlq_AREAqual.png')

    ##---------------------------------
    grass.run_command('r.out.ascii', input=landscape_grassname_frag_pid+'@MS_HABMAT_FRAG_PID', output='random_landscape_frag_pid.asc', null=0)
    grass.run_command('r.out.png', input=landscape_grassname_frag_pid+'@MS_HABMAT_FRAG_PID', output='random_landscape_frag_pid.png')

    grass.run_command('r.out.ascii', input=landscape_grassname_frag_AREApix+'@MS_HABMAT_FRAG_AREA' , output='random_landscape_frag_AREApix.asc', null=0)
    grass.run_command('r.out.png', input=landscape_grassname_frag_AREApix+'@MS_HABMAT_FRAG_AREA', output='random_landscape_frag_AREApix.png')

    grass.run_command('r.out.ascii', input=landscape_grassname_frag_AREAqual+'@MS_HABMAT_FRAG_AREAqual', output='random_landscape_frag_AREAqual.asc', null=0)
    grass.run_command('r.out.png', input=landscape_grassname_frag_AREAqual+'@MS_HABMAT_FRAG_AREAqual', output='random_landscape_frag_AREAqual.png')    

    #----------- DILA01
    ##---------------------------------
    grass.run_command('r.out.ascii', input=landscape_grassname_dila01clean_pid+'@MS_HABMAT_DILA01_PID',output='random_landscape_dila01clean_pid.asc', null=0)
    grass.run_command('r.out.png', input=landscape_grassname_dila01clean_pid+'@MS_HABMAT_DILA01_PID', output='random_landscape_dila01clean_pid.png')

    grass.run_command('r.out.ascii', input=landscape_grassname_dila01clean_AREApix+'@MS_HABMAT_DILA01_AREA', output='random_landscape_dila01clean_AREApix.asc', null=0)
    grass.run_command('r.out.png', input=landscape_grassname_dila01clean_AREApix+'@MS_HABMAT_DILA01_AREA', output='random_landscape_dila01clean_AREApix.png')

    grass.run_command('r.out.ascii', input=landscape_grassname_dila01clean_AREAqual.replace("HABMAT_grassclump_dila01_clean_AREAqual","HABMAT_DILA01_AREAqual")
+'@MS_HABMAT_DILA01_AREAqual', output='random_landscape_dila01clean_AREAqual.asc', null=0)
    grass.run_command('r.out.png', input=landscape_grassname_dila01clean_AREAqual.replace("HABMAT_grassclump_dila01_clean_AREAqual","HABMAT_DILA01_AREAqual")
+'@MS_HABMAT_DILA01_AREAqual', output='random_landscape_dila01clean_AREAqual.png')

    #----------- DILA02
    ##---------------------------------
    grass.run_command('r.out.ascii', input=landscape_grassname_dila02clean_pid+'@MS_HABMAT_DILA02_PID', output='random_landscape_dila02clean_pid.asc', null=0)
    grass.run_command('r.out.png', input=landscape_grassname_dila02clean_pid+'@MS_HABMAT_DILA02_PID', output='random_landscape_dila02clean_pid.png')

    grass.run_command('r.out.ascii', input=landscape_grassname_dila02clean_AREApix.replace("HQ_","")+'@MS_HABMAT_DILA02_AREA', output='random_landscape_dila02clean_AREApix.asc', null=0)
    grass.run_command('r.out.png', input=landscape_grassname_dila02clean_AREApix.replace("HQ_","")+'@MS_HABMAT_DILA02_AREA', output='random_landscape_dila02clean_AREApix.png')

    grass.run_command('r.out.ascii', input=landscape_grassname_dila02clean_AREAqual.replace("HABMAT_grassclump_dila02_clean_AREAqual","HABMAT_DILA02_AREAqual").replace("HQ_","")
+'@MS_HABMAT_DILA02_AREAqual', output='random_landscape_dila02clean_AREAqual.asc', null=0)
    grass.run_command('r.out.png', input=landscape_grassname_dila02clean_AREAqual.replace("HABMAT_grassclump_dila02_clean_AREAqual","HABMAT_DILA02_AREAqual").replace("HQ_","")
+'@MS_HABMAT_DILA02_AREAqual', output='random_landscape_dila02clean_AREAqual.png')
    
    
def export_raster_from_grass_userbase(landscape_grassname_habmat, landscape_grassname_hqmqlq, landscape_grassname_habdist, landscape_grassname_habmat_pid, landscape_grassname_habmat_areapix, landscape_grassname_hqmqlq_quality, landscape_grassname_hqmqlq_AREAqual, landscape_grassname_frag_pid, landscape_grassname_frag_AREApix,landscape_grassname_frag_AREAqual, landscape_grassname_dila01clean_pid, landscape_grassname_dila01clean_AREApix,landscape_grassname_dila01clean_AREAqual, landscape_grassname_dila02clean_pid, landscape_grassname_dila02clean_AREApix,landscape_grassname_dila02clean_AREAqual):
    '''This function read a set of filenames and export it from grass Mapsets 
    For this simulations, filename will be a list of _habmat, 
    _dist, _funcArea (several), _effectiveFuncArea
    '''

    ''' 
    An update was done in jan 2014 to fit with the new versions of GRASS 6.4.3
    
    '''
    
    #mycommands=[]

    grass.run_command("r.colors", map=landscape_grassname_habmat+'@userbase', rules='_habmat_color.txt')
    grass.run_command('r.out.ascii', input=landscape_grassname_habmat+'@userbase', output='random_landscape_habmat.asc')
    grass.run_command('r.out.png', input=landscape_grassname_habmat+'@userbase', output='random_landscape_habmat.png')
    
    grass.run_command('r.colors.stddev', input=landscape_grassname_habdist+'@userbase')
    grass.run_command('r.out.ascii', input=landscape_grassname_habdist+'@userbase', output='random_landscape_habdist.asc')
    grass.run_command('r.out.png', input=landscape_grassname_habdist+'@userbase', output='random_landscape_habdist.png')
    

    ##---------------------------------
    grass.run_command('r.out.ascii', input=landscape_grassname_habmat_pid+'@userbase',  output='random_landscape_habmat_pid.asc', null=0)
    grass.run_command('r.out.png', input=landscape_grassname_habmat_pid+'@userbase', output='random_landscape_habmat_pid.png')

    grass.run_command('r.out.ascii', input=landscape_grassname_habmat_areapix+'@userbase', output='random_landscape_habmat_areapix.asc', null=0)
    grass.run_command('r.out.png', input=landscape_grassname_habmat_areapix+'@userbase', output='random_landscape_habmat_areapix.png')
    
    
    ##---------------------------------
    grass.run_command('r.out.ascii', input=landscape_grassname_frag_pid+'@userbase', output='random_landscape_frag_pid.asc', null=0)
    grass.run_command('r.out.png', input=landscape_grassname_frag_pid+'@userbase', output='random_landscape_frag_pid.png')
    

    grass.run_command('r.out.ascii', input=landscape_grassname_frag_AREApix+'@userbase' , output='random_landscape_frag_AREApix.asc', null=0)
    grass.run_command('r.out.png', input=landscape_grassname_frag_AREApix+'@userbase', output='random_landscape_frag_AREApix.png')


    #----------- DILA01
    ##---------------------------------
    grass.run_command('r.out.ascii', input=landscape_grassname_dila01clean_pid+'@userbase',output='random_landscape_dila01clean_pid.asc', null=0)
    grass.run_command('r.out.png', input=landscape_grassname_dila01clean_pid+'@userbase', output='random_landscape_dila01clean_pid.png')

    grass.run_command('r.out.ascii', input=landscape_grassname_dila01clean_AREApix+'@userbase', output='random_landscape_dila01clean_AREApix.asc', null=0)
    grass.run_command('r.out.png', input=landscape_grassname_dila01clean_AREApix+'@userbase', output='random_landscape_dila01clean_AREApix.png')



    #----------- DILA02
    ##---------------------------------
    grass.run_command('r.out.ascii', input=landscape_grassname_dila02clean_pid+'@userbase', output='random_landscape_dila02clean_pid.asc', null=0)
    grass.run_command('r.out.png', input=landscape_grassname_dila02clean_pid+'@userbase_PID', output='random_landscape_dila02clean_pid.png')

    grass.run_command('r.out.ascii', input=landscape_grassname_dila02clean_AREApix.replace("HQ_","")+'userbase', output='random_landscape_dila02clean_AREApix.asc', null=0)
    grass.run_command('r.out.png', input=landscape_grassname_dila02clean_AREApix.replace("HQ_","")+'@userbase', output='random_landscape_dila02clean_AREApix.png')
    
    # devemos usar os mapas complete ?
    


