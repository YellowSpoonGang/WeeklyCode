2.2

Def kthtolast(List,kth):
    Head = list.head()
    Curr =head
    Length=0
    While curr.next!= Null:
       Curr = curr.next
       Length+=1
     position = Length - kth
     Curr = head
     For I=0 I<position I++:
        Curr = curr.next
     Return curr.value

2.3
Def deletemiddle(node):
    Next = node.next
    Node.value = next.value
    Node.next = next.next
    Next.next = None
