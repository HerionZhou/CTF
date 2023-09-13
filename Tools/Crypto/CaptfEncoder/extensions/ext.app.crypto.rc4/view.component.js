module.exports = {
    name: 'ext.app.crypto.rc4.view.component',
    data() {
        return {
            options: {
                value: {
                    key: '',
                    outputMode: 'BASE64'
                },
                schema: {
                    fields: [{
                        type: "text",
                        label: () => {
                            return this.$t("message.key")
                        },
                        key: "key",
                        cols: 3
                    }, {
                        type: "select",
                        label: () => {
                            return this.$t("message.output_mode")
                        },
                        key: "outputMode",
                        items: [{
                            text: "BASE64",
                            value: "BASE64"
                        }, {
                            text: "HEX",
                            value: "HEX"
                        }],
                        cols: 3

                    }]
                }
            }
        }
    },
    template: `
<ext-tab-encoder
    :title="$t('message.title')" 
    :options="options.value" 
    :schema="options.schema"
    encode="ext.app.crypto.rc4.encode" 
    decode="ext.app.crypto.rc4.decode"
    :encodeText="$t('message.encode_text')"
    :decodeText="$t('message.decode_text')">
</ext-tab-encoder>
`,
    i18n: require('./i18n')
}