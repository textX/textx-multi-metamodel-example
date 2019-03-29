from tkinter import Tk
import tkinter.ttk as ttk
from textx.const import MULT_OPTIONAL, MULT_ONE


def inspect(model, root=None, run_mainloop=True):

    print("inspect {}".format(model._tx_filename))
    if root is None:
        root = Tk()
        root.title(model._tx_filename)

    tree = ttk.Treeview(root)

    tree["columns"] = ("type", "attr")
    tree.column("type", width=200)
    tree.column("attr", width=200)
    tree.heading("type", text="type")
    tree.heading("attr", text="attr")

    def follow(elem, id="", is_link=False, attr_name=""):
        cls = elem.__class__
        if hasattr(cls, '_tx_attrs'):
            name = "<unnamed>"
            if hasattr(elem, 'name'):
                name = elem.name
            if hasattr(elem, '_tx_filename'):
                name = elem._tx_filename

            typename = cls.__name__
            if is_link:
                typename = "*{}".format(typename)
            new_id = tree.insert(id, 0, text=name,
                                 values=(typename, attr_name))

            if not is_link:
                for attr_name, attr in cls._tx_attrs.items():
                    if attr.mult in (MULT_ONE, MULT_OPTIONAL):
                        new_elem = getattr(elem, attr_name)
                        if new_elem:
                            follow(new_elem, new_id, not attr.cont,
                                   attr_name)
                    else:
                        new_elem_list = getattr(elem, attr_name)
                        if new_elem_list:
                            for new_elem in new_elem_list:
                                follow(new_elem, new_id, not attr.cont,
                                       attr_name)

            # problem: circular includes.
            # solution: open new window for new file?
            #
            # if hasattr(elem, '_tx_loaded_models'):
            #    new_id2 = tree.insert(new_id, 0, text=name,
            #                          values=("list", "included model"))
            #    for m in elem._tx_loaded_models:
            #        follow(m, new_id2)

    follow(model)

    tree.pack()
    if run_mainloop:
        root.mainloop()

    return root
