<template>
    <div id="app">
      <TodoHeader></TodoHeader>
      <TodoInput v-on:addTodo="addTodo"></TodoInput>
      <TodoFooter v-on:removeAll="clearAll"></TodoFooter>
      <TodoList v-bind:propsdata="todoItems"></TodoList>
    </div>
</template>

<script>
import TodoHeader from './components/TodoHeader.vue'
import TodoInput from './components/TodoInput.vue'
import TodoFooter from './components/TodoFooter.vue'
import TodoList from './components/TodoList.vue'

export default {
  data() {
    return  {
      todoItems: []
    }
  },

  created() {
    if (localStorage.length > 0) {
        for (var i = 0; i < localStorage.length; i++) {
              this.todoItems.push(localStorage.key(i));
        }
    }
  },

  methods: {
    addTodo() {
      localStorage.setItem(todoItem, todoItem);
      this.todoItems.push(todoItem);
    },
    clearAll() {
      localStorage.clear();
      this.todoItems = [];
    },
  },

  components: {
    'TodoHeader' : TodoHeader,
    'TodoInput' : TodoInput,
    'TodoFooter' : TodoFooter,
    'TodoList' : TodoList
  }
}
</script>

<style>
    body {
        text-align: center;
        background-color: #F6F6F8;
    }
    input {
        border-style: groove;
        width: 200px;
    }
    button {
        border-style: groove;
    }
    .shadow {
        box-shadow: 5px 10px 10px rgba(0, 0, 0, 0.03)
    }
</style>