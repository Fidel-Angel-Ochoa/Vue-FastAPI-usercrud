<template>
    <v-col >
        <v-col>
            <Form/>
        </v-col>
        <v-col>
            <Table/>
        </v-col>
    </v-col>
</template>

<script>
import Table from '../components/Table.vue';
import Form from '../components/Form.vue';

 
export default {
    components: { Table, Form }
}
</script>
