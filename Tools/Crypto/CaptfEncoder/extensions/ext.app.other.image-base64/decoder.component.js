
module.exports = {
    name: 'decoder',
    data() {
        return {
            input: '',
            output: ''
        }
    },
    template: `           
<v-container fluid class="ma-2">  
    <v-row class="mx-2">
        <v-spacer></v-spacer>
        <v-btn elevation="2" @click="saveFile" text >{{$t("message.save_as")}}</v-btn>       
    </v-row>
    <v-row>
        <v-col>
            <ext-editor v-model="input" :label="$t('message.input')">
            </ext-editor>
        </v-col>
        <v-col>
            <v-card class="mx-auto">
                <v-img :src="input"></v-img>
            </v-card>
        </v-col>
    </v-row>
</v-container>           
`,
    i18n: require('./i18n'),
    methods: {
        async saveFile() {
            const result = await this.$extInvoke('ext.app.other.image-base64.decode', this.input);

            if (result && result.success) {
                const fileData = result.output;

                await this.$saveImageFile(fileData.data, fileData.extension, this.$t('message.dialog_save_as'));
            } 
        }

    }
}