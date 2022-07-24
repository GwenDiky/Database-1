# Generated by Django 4.0.6 on 2022-07-24 20:21

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirstDispute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('01 О заключении, изменении и расторжении договоров', '01 О заключении, изменении и расторжении договоров'), ('02 О недействительности сделок', '02 О недействительности сделок'), ('03 О неисполнении или ненадлежащем исполнении обязательств по договорам', '03 О неисполнении или ненадлежащем исполнении обязательств по договорам'), ('04 Внедоговорные обязательства', '04 Внедоговорные обязательства'), ('05 О проверке законности нормативных актов, действий(бездействий) государственных органов, должностных лиц', '05 О проверке законности ненормативных актов, действий (бездействий) государственных органов, должностных лиц'), ('06 О признании права собственности', '06 О признании права собственности'), ('07 Об истребовании имущества из чужого незаконного владения (виндикационный иск)', '07 Об истребовании имущества из чужого незаконного владения (виндикационный иск)'), ('08 О нарушении прав, не связанных с лишением владения (негаторный иск)', '08 О нарушении прав, не связанных с лишением владения (негаторный иск)'), ('09 О признании не подлежащим исполнению исполнительного документа, по которому взыскание производится в бесспорном порядке', '09 О признании не подлежащим исполнению исполнительного документа, по которому взыскание производится в бесспорном порядке'), ('10 О взыскании налогов, сборов, экономических санкций, других обязательных платежей в бюджет', '10 О взыскании налогов, сборов, экономических санкций, других обязательных платежей в бюджет'), ('11 О возврате из бюджета и государственных внебюджетных фондов денежных средств, списанных в бесспорном порядке', '11 О возврате из бюджета и государственных внебюджетных фондов денежных средств, списанных в бесспорном порядке'), ('12 О ликвидации юридических лиц', '12 О ликвидации юридических лиц'), ('13 О привлечении к субсидиарной ответственности', '13 О привлечении к субсидиарной ответственности'), ('14 О прекращении деятельности индивидуальных предпринимателей', '14 О прекращении деятельности индивидуальных предпринимателей'), ('15 Об экономической несостоятельности (банкротстве)', '15 Об экономической несостоятельности (банкротстве)'), ('16 О защите деловой репутации', '16 О защите деловой репутации'), ('17 Об установлении фактов, имеющих юридическое значение', '17 Об установлении фактов, имеющих юридическое значение'), ('18', '18'), ('19 По жалобам на нотариальные действия или отказ в их совершении', '19 По жалобам на нотариальные действия или отказ в их совершении'), ('20 Нарушение законодательства об охране окружающей среды', '20 Нарушение законодательства об охране окружающей среды'), ('21 Учредительство', '21 Учредительство'), ('22 О понуждении совершить определённые действия', '22 О понуждении совершить определённые действия'), ('23 Иные категории', '23 Иные категории'), ('24 Обжалование ответов на обращения юридических лиц, индивидуальных предпринимателей или граждан', '24 Обжалование ответов на обращения юридических лиц, индивидуальных предпринимателей или граждан'), ('25 О продлении приостановления (запрета) деятельности по заявлениям контролирующих органов', '25 О продлении приостановления (запрета) деятельности по заявлениям контролирующих органов'), ('26 О приостановлении деятельности по заявлениям контролирующих органов', '26 О приостановлении деятельности по заявлениям контролирующих органов'), ('27 Споры в отношении находящегося в государственной собственности имущества', '27 Споры в отношении находящегося в государственной собственности имущества'), ('28 По жалобам на действия судебного исполнителя', '28 По жалобам на действия судебного исполнителя'), ('29 О возбуждении приказного производства ', '29 О возбуждении приказного производства '), ('30 О взыскании денежных средств', '30 О взыскании денежных средств'), ('31  О выдаче исполнительного документа', '31 О выдаче исполнительного документа'), ('32  О выдаче исполнительного документа на принудительное исполнение медиативного соглашения', '32 О выдаче исполнительного документа на принудительное исполнение медиативного соглашения'), ('33  О признании и приведении в исполнение решений иностранных судов на территории Республики Беларусь', '33 О признании и приведении в исполнение решений иностранных судов на территории Республики Беларусь')], max_length=122, verbose_name='Категория спора (подкатегория 1):')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, validators=[django.core.validators.MinLengthValidator(main.models.get_min_length, message='Для продолжения работы с формой необходимо ввести минимум 10 символов')], verbose_name='Наименование постановления')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('case_number', models.CharField(default='Неизвестно', max_length=40, validators=[django.core.validators.MinLengthValidator(main.models.get_min_length_case_number, message='Для продолжения работы с формой необходимо ввести минимум 3 символа')], verbose_name='Номер дела:')),
                ('documents', models.URLField(blank=True, max_length=300, null=True, validators=[django.core.validators.URLValidator(code=None, message=None, regex=None, schemes=None)], verbose_name='Связанные документы (ссылки):')),
                ('trial', models.CharField(choices=[('Верховный суд Республики Беларусь', 'Верховный суд Ресублики Беларусь'), ('Экономический суд Брестской области', 'Экономический суд Брестской области'), ('Экономический суд Витебской области', 'Экономический суд Витебской области'), ('Экономический суд Гомельской области', 'Экономический суд Гомельской области'), ('Экономический суд Гродненской области', 'Экономический суд Гродненской области'), ('Экономический суд города Минска', 'Экономический суд города Минска'), ('Экономический суд Минской области', 'Экономический суд Минской области'), ('Экономический суд Могилевской области', 'Экономический суд Могилевской области')], default='Верховный суд Ресублики Беларусь', max_length=37, verbose_name='Наименование суда')),
                ('instance', models.CharField(choices=[('Первая', 'Первая'), ('Апеляционная', 'Апеляционная'), ('Кассационная', 'Кассационная'), ('Надзорная', 'Надзорная')], default='Первая', max_length=12, verbose_name='Инстанция:')),
                ('intial', models.CharField(blank=True, choices=[('Удовлетворено', 'Удовлетворено'), ('Удовлетворено в части', 'Удовлетворено в части'), ('Отказано', 'Отказано')], max_length=200, null=True, verbose_name='Первоначальное решение первой инстанции')),
                ('counter', models.CharField(blank=True, choices=[('Удовлетворено', 'Удовлетворено'), ('Удовлетворено в части', 'Удовлетворено в части'), ('Отказано', 'Отказано')], max_length=200, null=True, verbose_name='Встречное решение первой инстанции')),
                ('appellate', models.CharField(blank=True, choices=[('Нет', 'Нет'), ('Изменено', 'Изм.'), ('Отказано', 'Отк.')], max_length=200, null=True, verbose_name='Решение апелляционной инстанции')),
                ('cassation', models.CharField(blank=True, choices=[('Нет', 'Нет'), ('Изменено', 'Изм.'), ('Отказано', 'Отк.')], max_length=200, null=True, verbose_name='Решение кассационной инстанции')),
                ('proceeding', models.CharField(choices=[('Административное', 'Административное'), ('Интеллектуальное', 'Интеллектуальное'), ('Экономическое', 'Экономическое')], default='Административное', max_length=16, verbose_name='Вид судопроизводства:')),
                ('second1_dispute', models.CharField(blank=True, choices=[('None', 'Выбирается при значения "Подкатегория 1" - "01 О заключении, изменении и расторжении договоров"'), ('01.01 о понуждении к заключению договора', '01.01 о понуждении к заключению договора'), ('01.02 о разногласиях по условиях договора', '01.02 о разногласиях по условиях договора'), ('01.03 об изменении условий договора', '01.03 об изменении условий договора'), ('01.04 о расторжении договора', '01.04 о расторжении договора'), ('01.05 о расторжении договора и выселении', '01.05 о расторжении договора и выселении'), ('01.06 о признании недействительным (неправомерным) одностороннего отказа от договора', '01.06 о признании недействительным (неправомерным) одностороннего отказа от договора'), ('01.07 о признании договора незаключённым', '01.07 о признании договора незаключённым')], max_length=122, null=True, verbose_name='Категория спора (подкатегория 2-1)')),
                ('second2_dispute', models.CharField(blank=True, choices=[('None', 'Выбирается при значения "Подкатегория 1" - "02 О недействительности сделок"'), ('02.01 о признании сделки недействительной', '02.01 о признании сделки недействительной'), ('02.02 о применении последствий недействительности сделки', '02.02 о применении последствий недействительности сделки'), ('02.03 о признании торгов недействительными', '02.03 о признании торгов недействительными'), ('02.04 об установлении факта ничтожности сделки', '02.04 об установлении факта ничтожности сделки'), ('02.05 о применении последствий ничтожности сделки', '02.05 о применении последствий ничтожности сделки')], max_length=122, null=True, verbose_name='Категория спора (подкатегория 2-2)')),
                ('third_dispute', models.CharField(blank=True, choices=[('None', 'Выбирается при значениях "Подкатегория 1" - "02 О недействительности сделок" и "Подкатегория 2" - "02.03 о признании торгов недействительными"'), ('02.03.01 о признании незаконными решения и (или) действия (бездействия) организации либо членов комиссии', '02.03.01 о признании незаконными решения и (или) действия (бездействия) организации либо членов комиссии'), ('02.03.02 иные споры о признании торгов недействительными', '02.03.02 иные споры о признании торгов недействительными')], max_length=122, null=True, verbose_name='Категория спора (подкатегория 3)')),
                ('motivation', models.CharField(blank=True, choices=[('Есть', 'Есть'), ('Нет', 'Нет')], max_length=4, null=True, verbose_name='Наличие мотивировочное части:')),
                ('review', models.CharField(blank=True, choices=[('Есть', 'Есть'), ('Нет', 'Нет')], max_length=4, null=True, verbose_name='История рассмотрения:')),
                ('original_claim', models.CharField(default='Не значится', max_length=300, verbose_name='Первоначальное требование:')),
                ('counter_claim', models.CharField(default='Не значится', max_length=300, verbose_name='Встречное требование:')),
                ('description', models.TextField(default='Полное постановление отсутствует.', verbose_name='Полное постановление')),
                ('upload', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/')),
                ('first_dispute', models.ManyToManyField(default='01 О заключении, изменении и расторжении договоров', to='main.firstdispute')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]