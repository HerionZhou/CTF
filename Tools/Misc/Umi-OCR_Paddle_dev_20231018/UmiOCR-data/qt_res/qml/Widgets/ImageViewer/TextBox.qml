// =============================================
// =============== 单个文本块组件 ===============
// =============================================

import QtQuick 2.15
import QtQuick.Controls 2.15
import ".."

Item {
    id: tRoot
    property string text: ""

    // 颜色固定，不受主题影响
    property color bgColor: "#99000000"
    property color textColor: "#FFFFFF"

    // 外部接口，重设字体和组件大小
    property var resetSize: textEdit.resetFontSize
    property alias textEdit: textEdit // 文本组件

    // 传入一个相对于item的坐标，返回该坐标的文本序号。
    function where(item, mx, my) {
        const textPoint = textEdit.mapFromItem(item, mx, my)
        const textPos = textEdit.positionAt(textPoint.x, textPoint.y)
        return textPos
    }

    // 背景
    Rectangle {
        id: bgRect 
        anchors.fill: parent
        color: bgColor
    }
    // 文本
    TextEdit_ {
        id: textEdit
        anchors.fill: parent
        color: textColor
        readOnly: true // 只读
        selectByMouse: false // 禁止选择文本
        selectByKeyboard: false
        persistentSelection: true // 丢失焦点时，保留选区
        font.pixelSize: 10 // 初始：10像素
        
        // 重设字体大小，以适合组件大小
        function resetFontSize() {
            text = tRoot.text
            // 初次调整，利用初始文字面积与容器面积的比值，计算字体大小
            let s = 1
            if(contentWidth>0 && contentHeight>0)
                s = (width * height) / (contentWidth * contentHeight)
            let ps = font.pixelSize * Math.sqrt(s)
            font.pixelSize = ps
            // 二次调整，如果文本比容器高出至少1行，则减小字体大小，直到不高于容器
            if(contentHeight >= height+ps) {
                // 为了保持性能，限定调整的最大次数
                for(let i=0; i<10 && contentHeight > height; i++) {
                    font.pixelSize--
                }
            }
            // 最终让整体宽高与文本块相同
            tRoot.width = contentWidth
            tRoot.height = contentHeight
        }
    }
}