# 素材来源与许可核实

2026-10-14 核对。事实、证据与本项目适用范围分别列出；不把下游仓库的代码许可证直接解释为插画授权。

| 核实项目 | 原始证据 | 本次读取结果与边界 |
| --- | --- | --- |
| 鲸鱼娘原角色 | [上善无形 B站动态](https://www.bilibili.com/opus/1231977657712771073) | 本次成功读取到原作者关于鲸鱼娘形象的 CC BY-NC-SA 4.0 声明。 |
| 女仆 DeepSeek / Claude / GPT 原型 | [ZipZipPipe《AI娘化》](https://www.pixiv.net/artworks/148186519)、[公开元数据接口](https://www.pixiv.net/ajax/illust/148186519)、[图页接口](https://www.pixiv.net/ajax/illust/148186519/pages) | 接口确认作者ID18604994、作品ID148186519、17张图；本地视觉核对 p2 为本次橙发 Claude 原型、p3 为白龙娘 GPT 原型。说明要求署名和非商业使用，DeepSeek 的特定形象另明确遵循上善的 CC BY-NC-SA 4.0。不是将这一项 CC 声明推广到全部17张图。 |
| GitHub 参考收录 | [WPH666-py README](https://github.com/WPH666-py/AI-Family-Skin-Suit3/blob/main/README.md)、[LICENSE](https://github.com/WPH666-py/AI-Family-Skin-Suit3/blob/main/LICENSE) | README 的素材说明限定个人桌面美化、禁止二次商用；LICENSE 是软件 MIT。本项目保留其收录出处，原角色署名以原作者证据为准。 |
| DeepSeek 下游署名链范例 | [Small-tailqwq NOTICE](https://github.com/Small-tailqwq/dsh-deep-whale/blob/main/maid-atelier/NOTICE)、[美术许可](https://github.com/Small-tailqwq/dsh-deep-whale/blob/main/maid-atelier/LICENSE-ARTWORK)、[代码许可范围](https://github.com/Small-tailqwq/dsh-deep-whale/blob/main/LICENSE) | 明确分开代码 MIT 与美术 CC BY-NC-SA 4.0；完整署名上善、ZipZipPipe 及其自身贡献。本项目保留 NOTICE 与美术许可全文作为链路参考。 |
| 逐文件组织范例 | [JAdpp NOTICE](https://github.com/JAdpp/dsh-whale-galgame/blob/main/NOTICE.md) | 参考其逐文件来源、改动、许可与商标说明的做法。本项目未将其另款 Claude/GPT 的 CC 授权挪用到本次不同原型。 |
| 证据边界组织范例 | [yifanchen12 ASSET_SOURCES](https://github.com/yifanchen12/wrap-me-in-plastic-gpt-codex-pv/blob/main/docs/ASSET_SOURCES.md) | 参考其把原作者声明、下游说明、改动及未核实范围分别记录的方式。其 PV、音乐和 MMD 资料不属于本项目资产。 |
| CC 条款 | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) | 保留署名、许可链接及改动说明；非商业；相应改编同协议。不会以本仓库的私有设置取消授权接收者已经拥有的 CC 权利。 |

## 衣服、学校与品牌参考

Claude 服装曾参考 [品川女子学院官方校服图](https://www.shinagawajoshigakuin.jp/schoollife/uniform/) 的毛衣、领带和章的位置，随后改为角色配色。GPT 毛衣、皮裙、1460靴和项链材质参考由用户提供照片。原始参考照片没有随此仓库重新发布；这些参考也不表示取得学校、品牌或商品照片的商业授权。

## 图像改编清单

三视图和独立素材的清单、原文件SHA-256及本地制作记录随每个角色目录保存。DeepSeek 使用 v12 五指正面，Claude 使用白色粗描边刺绣章及 v6 完整分层背面，GPT 使用最后确认的独立项链拼接与两层背面。

主目录中的大幅master保留真实alpha；原图与已对齐层分开命名。完整躯干＋完整头发合成、项链/刺绣章合成均可通过 recompose.py 复现，并已与终稿逐像素验证。

## 当前分发方式

用户指定私有仓库完整归档。本次没有公开发布仓库，也没有为全部人物插画统一套用开源代码许可证。角色原型、标识和改编部分各自保留适用权利；公开传播和商业使用的条件须根据原始条款再核对。
