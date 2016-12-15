import logging
from flask_principal import AnonymousIdentity
from flask import request
from flask import current_app
from flask import g

import user_agents

logger =logging.getLogger(__name__)

def test_jira_api(args):
    logger.info(str(args))
    if not isinstance(g.identity, AnonymousIdentity):
        raw_ua = request.headers.get('User-Agent') or ''
        ua = user_agents.parse(raw_ua)
        args['os'] = ua.os.family
        args['browser'] = ua.browser.family
        args['device'] = ua.device.family
        args['ua'] = raw_ua
    from jira import JIRA

    HOST = current_app.config['JIRA_HOST']
    BASIC_AUTH_USER = current_app.config['BASIC_AUTH_USER']
    BASIC_AUTH_PASSWORD = current_app.config['BASIC_AUTH_PASSWORD']
    PROJECT = current_app.config['PROJECT']
    EPIC = current_app.config['EPIC']
    # 权限
    jira = JIRA(HOST, basic_auth=(BASIC_AUTH_USER, BASIC_AUTH_PASSWORD))
    # 新建issue
    new_issue = jira.create_issue(project=PROJECT, summary=args['summary'],
                                  description=args.get('description', ''), issuetype={'name': args['type']})
    # 添加issue到epic
    jira.add_issues_to_epic(EPIC, [str(new_issue.key)])
    # 添加额外信息到comment
    display_list = ['summary', 'description', 'type', 'file']
    comment_body = ''.join(['%s:%s \n' % (k, args[k]) for k in args if k not in display_list])
    jira.add_comment(new_issue.key, comment_body) if comment_body else ""
    # 添加附件
    data = request.files.getlist("file")
    current_app.logger.info(type(data))
    if data:
        for file_data in data:
            current_app.logger.info(file_data.filename)
            binary = file_data.stream.read()
            if binary:
                jira.add_attachment(issue=new_issue, attachment=binary, filename=str(uuid.uuid1())+'.'+file_data.filename.split(".")[-1])