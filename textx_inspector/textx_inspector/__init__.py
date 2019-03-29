#from Tkinter import *
from tkinter import *
import tkinter.ttk as ttk
from textx.const import MULT_OPTIONAL, MULT_ONE, MULT_ONEORMORE, \
    MULT_ZEROORMORE, RULE_ABSTRACT, RULE_MATCH, MULT_ASSIGN_ERROR, \
    UNKNOWN_OBJ_ERROR

def inspect(model, root=None, run_mainloop=True):

    print("inspect {}".format(model._tx_filename))
    if root is None:
        root = Tk()
        root.title(model._tx_filename)

    tree = ttk.Treeview(root)

    tree["columns"]=("type","attr_type")
    tree.column("type", width=100 )
    tree.column("attr_type", width=100)
    tree.heading("type", text="type")
    tree.heading("attr_type", text="attr type")

    #tree.insert("" , 0,    text="Line 1", values=("1A","1b"))

    #id2 = tree.insert("", 1, "dir2", text="Dir 2")
    #tree.insert(id2, "end", "dir 2", text="sub dir 2", values=("2A","2B"))

    ##alternatively:
    #tree.insert("", 3, "dir3", text="Dir 3")
    #tree.insert("dir3", 3, text=" sub dir 3",values=("3A"," 3B"))

    def follow(elem, id="", is_link=False):
        cls = elem.__class__
        if hasattr(cls, '_tx_attrs'):
            name = "<unnamed>"
            if hasattr(elem,'name'):
                name = elem.name

            typename = cls.__name__
            if is_link:
                typename = "*{}".format(typename)
            new_id = tree.insert(id, 0, text=name, values=(typename, "todo"))

            if not is_link:
                for attr_name, attr in cls._tx_attrs.items():
                    if attr.mult in (MULT_ONE, MULT_OPTIONAL):
                        new_elem = getattr(elem, attr_name)
                        if new_elem:
                            follow(new_elem, new_id, not attr.cont)
                    else:
                        new_elem_list = getattr(elem, attr_name)
                        if new_elem_list:
                            for new_elem in new_elem_list:
                                follow(new_elem, new_id, not attr.cont)

    follow(model)

    tree.pack()
    if run_mainloop:
        root.mainloop()

    return root

