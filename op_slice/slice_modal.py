'''
Created on Oct 8, 2015

@author: Patrick
'''
from ..modaloperator import ModalOperator
from .slice_ui           import Slice_UI
from .slice_ui_modalwait  import Slice_UI_ModalWait
from .slice_ui_draw       import Slice_UI_Draw


class CGC_Slice(ModalOperator, Slice_UI, Slice_UI_ModalWait, Slice_UI_Draw):
    ''' CG Cookie Polytrim Modal Editor '''
    ''' Note: the functionality of this operator is split up over multiple base classes '''
    
    operator_id    = "cgcookie.slice"       # operator_id needs to be the same as bl_idname
                                            # important: bl_idname is mangled by Blender upon registry :(
    bl_idname      = "cgcookie.slice"
    bl_label       = "Slice"
    bl_space_type  = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    
    def __init__(self):
        FSM = {}
        #FSM['sketch']  = self.modal_sketch
        FSM['grab']    = self.modal_grab
        #FSM['inner']   = self.modal_inner

        ModalOperator.initialize(self, FSM)
    
    def start_poll(self, context):
        ''' Called when tool is invoked to determine if tool can start '''
                
        if context.mode != 'OBJECT':
            #show_error_message('Object Mode please')
            return False
        
        if context.object.type != 'MESH':
            #show_error_message('Must select a mesh object')
            return False
        
        return True
    
    def start(self, context):
        ''' Called when tool is invoked '''
        self.start_ui(context)
    
    def end(self, context):
        ''' Called when tool is ending modal '''
        self.end_ui(context)
    
    def end_commit(self, context):
        ''' Called when tool is committing '''
        self.cleanup(context, 'commit')
    
    def end_cancel(self, context):
        ''' Called when tool is canceled '''
        self.cleanup(context, 'cancel')
        pass
    
    def update(self, context):
        pass