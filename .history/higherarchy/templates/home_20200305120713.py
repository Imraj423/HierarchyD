{% load mptt_tags % }
<ul >
    {% recursetree genres % }
       <li >
            {{node.name}}
            {% if not node.is_leaf_node % }
                <ul class = "children" >
                    {{children}}
                </ul >
            {% endif % }
        </li >
    { % endrecursetree % }
</ul >
