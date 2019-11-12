Vue.component('todo-footer', {
    template: '<p>This is another global child component</p>'
});

var cmp = {
    template: '<p>This is another local child component</p>'
};

var app = new Vue({
    el: '#app',
    data: {
        message: 'parent component'
    },
    components: {
        'todo-list': cmp
    }
});

var cmp1 = {
    template: '<div>첫 번째 지역 컴포넌트: {{ cmp1Data }}</div>',
    data () {
        return {
            cmp1Data: 100
        }
    }
};

var cmp2 = {
    template: '<div>두 번째 지역 컴포넌트: {{ cmp2Data }}</div>',
    data () {
        return {
            cmp2Data: cmp1.data.cmp1Data
        }
    }
};

var app2 = new Vue({
    el: '#app-2',
    data: {
        message: 'props test'
    },
    components: {
        'my-cmp1': cmp1,
        'my-cmp2': cmp2 
    }
});