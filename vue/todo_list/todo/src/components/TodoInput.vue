<template>
    <div class="inputBox shadow">
        <input type="text" v-model="newToDoItem" placeholder="Type what you have to do" v-on:keyup.enter="addTodo">
        <span class="addContainer" v-on:click="addTodo">
            <i class="addBtn fas fa-plus" aria-hidden="true"></i>
        </span>
    </div>
</template>

<script>
export default {
    data() {
        return {
            newToDoItem: '',
        }
    },
    methods: {
        addTodo() {
            console.log(this.newToDoItem);
            if (this.newToDoItem !== "") {
                var value = this.newToDoItem && this.newToDoItem.trim();
                this.$emit('addTodo', value);
                this.clearInput();
            }
        },
        clearInput() {
            this.newToDoItem = '';
        }
    }
}
</script>

<style scioed>
    input:focus {
        outline: none;
    }
    .inputBox {
        background: white;
        height: 50px;
        line-height: 50px;
        border-radius: 5px;
    }
    .inputBox input {
        border-style: none;
        font-size: 0.9rpm;
    }
    .addContainer {
        float: right;
        background: linear-gradient(to right, #6478fb, #8763fb);
        display: block;
        width: 3rem;
        border-radius: 0 5px 5px 0;
    }
    .addBtn {
        color: white;
        vertical-align: middle;
    }
</style>