from talon.voice import Context, Rep, talon, generic
from user.utils import parse_words_as_integer

class MyRep(generic):
   def __call__(self, m):
       tmp = []
       if self.ctx.last_action:
           for action, rule in self.ctx.last_action:
               for i in range(self.data):
                   act = action(rule) or (action, rule)
               tmp.append(act)
       return tmp

ctx = Context('repeater')


def repeat(m):
   repeat_count = parse_words_as_integer(m._words[1:])

   if repeat_count != None and repeat_count >= 1:
       repeater = MyRep(repeat_count)
       repeater.ctx = talon
       return repeater(None)

ctx.keymap({
   'ouno': MyRep(1),
   'doss': MyRep(2),
   'trace': MyRep(3),
   'cutroo': MyRep(4),
   'sincko': MyRep(5),
   'seis': MyRep(6),
   'siete': MyRep(7),
   'ottchou': MyRep(8),
   'noueve': MyRep(9),
   'diez': MyRep(10),
   'repeat (0 | oh | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)+': repeat,
})